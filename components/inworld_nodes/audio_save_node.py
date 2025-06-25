import comfy.utils
from engines.inworld_tts.utils import save_audio_file, validate_audio_format, get_audio_info


class InworldAudioSaveNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
                "filename": ("STRING", {"default": "output.wav"}),
                "output_dir": ("STRING", {"default": "outputs"}),
            },
            "optional": {
                "show_info": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("file_path",)
    FUNCTION = "run"
    TITLE = "Inworld Audio Save"

    CATEGORY = "Inworld/TTS"
    DESCRIPTION = "Save audio bytes to a file with validation"

    def __init__(self):
        pass

    def run(self, **kwargs):
        audio = kwargs["audio"]
        filename = kwargs["filename"]
        output_dir = kwargs["output_dir"]
        show_info = kwargs.get("show_info", True)
        
        if audio is None:
            print("No audio data to save")
            return ("",)
        
        # Validate audio format
        if not validate_audio_format(filename):
            print(f"Warning: Audio format may not be supported for file: {filename}")
        
        try:
            # Save audio file using utility function
            file_path = save_audio_file(audio, filename, output_dir)
            
            if show_info:
                # Get and display audio info
                sample_rate, channels, duration = get_audio_info(audio)
                if sample_rate:
                    print(f"Audio saved to: {file_path}")
                    print(f"  Sample rate: {sample_rate} Hz")
                    print(f"  Channels: {channels}")
                    print(f"  Duration: {duration:.2f} seconds")
                    print(f"  Size: {len(audio)} bytes")
                else:
                    print(f"Audio saved to: {file_path} (Size: {len(audio)} bytes)")
            else:
                print(f"Audio saved to: {file_path}")
                
            return (file_path,)
            
        except Exception as e:
            print(f"Error saving audio: {str(e)}")
            return ("",) 