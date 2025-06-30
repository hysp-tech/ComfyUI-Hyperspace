import comfy.utils
from ...engines.inworld_tts.utils import get_audio_info


class InworldAudioPreviewNode:
    OUTPUT_NODE = True

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
            },
            "optional": {
                "show_info": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "preview"
    TITLE = "Inworld Audio Preview"
    CATEGORY = "Inworld"
    DESCRIPTION = "Preview audio with detailed information"

    def __init__(self):
        pass

    def preview(self, **kwargs):
        audio = kwargs["audio"]
        if audio is None:
            print("No audio data to preview")
            return

        try:
            waveform = audio["waveform"]
            sample_rate = audio["sample_rate"]

            # Get information from tensor
            num_samples = waveform.shape[-1]
            channels = waveform.shape[1]
            duration = num_samples / sample_rate

            print(f"Audio Preview Info: {''}")
            print(f"  Sample rate: {sample_rate} Hz")
            print(f"  Channels: {channels}")
            print(f"  Duration: {duration:.2f} seconds")
            print(f"  Tensor shape: {list(waveform.shape)}")

            # ComfyUI frontend will automatically handle preview. This node is now mainly used to print information to the console.
            # Because RETURN_TYPES is empty, nothing is returned here.
            # If you want to pass the audio down, you can change RETURN_TYPES to ("AUDIO",) and return (audio,)

        except Exception as e:
            print(f"Error previewing audio: {str(e)}")
