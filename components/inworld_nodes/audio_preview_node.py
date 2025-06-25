import comfy.utils
from engines.inworld_tts.utils import get_audio_info


class InworldAudioPreviewNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
            },
            "optional": {
                "show_info": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("audio",)
    FUNCTION = "run"
    TITLE = "Inworld Audio Preview"

    CATEGORY = "Inworld/TTS"
    DESCRIPTION = "Preview audio bytes with detailed information"

    def __init__(self):
        pass

    def run(self, **kwargs):
        audio = kwargs["audio"]
        show_info = kwargs.get("show_info", True)
        
        if audio is None:
            print("No audio data to preview")
            return (None,)
        
        try:
            if show_info:
                # Get and display detailed audio info
                sample_rate, channels, duration = get_audio_info(audio)
                if sample_rate:
                    print(f"Audio Preview:")
                    print(f"  Sample rate: {sample_rate} Hz")
                    print(f"  Channels: {channels}")
                    print(f"  Duration: {duration:.2f} seconds")
                    print(f"  Size: {len(audio)} bytes")
                    print(f"  Format: {'Stereo' if channels == 2 else 'Mono'} WAV")
                else:
                    print(f"Audio preview ready - Size: {len(audio)} bytes")
            else:
                print(f"Audio preview ready - Size: {len(audio)} bytes")
                
            # For ComfyUI preview, we just pass through the audio
            # The ComfyUI interface will handle the preview automatically
            return (audio,)
            
        except Exception as e:
            print(f"Error previewing audio: {str(e)}")
            return (None,) 