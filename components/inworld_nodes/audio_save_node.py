import torch
import torchaudio
import os
import comfy.utils
from comfy.sd import (
    VAE,
)  # Just to prevent torchaudio.save from erroring, as ComfyUI environment might not have torch audio by default


# Ensure output directory exists
def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


class InworldAudioSaveNode:
    # Mark as output node so it can serve as workflow endpoint
    OUTPUT_NODE = True

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
                # Using ComfyUI built-in directory and filename widgets would be better
                "output_dir": ("STRING", {"default": "output/audio"}),
                "filename_prefix": ("STRING", {"default": "InworldAudio"}),
            },
            "ui": {
                # Hide file path output in UI since it's mainly for backend use
                "file_path": ("STRING", {"visible": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("file_path",)
    FUNCTION = "save"
    TITLE = "Inworld Audio Save"
    CATEGORY = "Inworld/Audio"
    DESCRIPTION = "Save audio data to a file (e.g., WAV)."

    def save(self, audio, output_dir, filename_prefix):
        if audio is None or "waveform" not in audio or "sample_rate" not in audio:
            print(
                "Error: Invalid audio data received. Expected a dictionary with 'waveform' and 'sample_rate'."
            )
            return ("",)

        try:
            # 1. Unpack data from AUDIO dictionary
            waveform = audio["waveform"]  # Tensor [batch, channels, samples]
            sample_rate = audio["sample_rate"]  # int

            # Ensure output directory exists
            full_output_dir = os.path.join(
                comfy.application.get_output_directory(), output_dir
            )
            ensure_dir_exists(full_output_dir)

            # Prepare filename and path
            # Use ComfyUI's method to generate numbered filenames to avoid overwriting
            (
                full_path,
                filename,
                counter,
                subfolder,
                _,
            ) = comfy.utils.get_save_image_path(
                filename_prefix, full_output_dir, waveform.shape[0]
            )

            # Complete file path (using .wav extension)
            file_path = f"{full_path}_{counter:05}.wav"

            # 2. Save Tensor as WAV file
            # torchaudio.save requires waveform format [channels, samples]
            # Our waveform is [batch, channels, samples], so take the first batch item
            # If batch > 1, you might need a loop to save multiple files
            waveform_to_save = waveform[0]

            torchaudio.save(file_path, waveform_to_save, sample_rate)

            # 3. Print information
            channels = waveform_to_save.shape[0]
            duration = waveform_to_save.shape[1] / sample_rate
            size_bytes = os.path.getsize(file_path)

            print(f"Audio saved to: {file_path}")
            print(f"  Sample rate: {sample_rate} Hz")
            print(f"  Channels: {channels}")
            print(f"  Duration: {duration:.2f} seconds")
            print(f"  Size: {size_bytes / 1024:.2f} KB")

            # Return file path, can display more information in UI through dictionary format
            # ComfyUI frontend can parse this dictionary to display links
            result = {
                "ui": {"text": [f"Saved to {os.path.relpath(file_path)}"]},
                "result": (file_path,),
            }
            return result  # Return dictionary instead of tuple

        except Exception as e:
            print(f"Error saving audio: {e}")
            import traceback

            traceback.print_exc()
            return ("",)
