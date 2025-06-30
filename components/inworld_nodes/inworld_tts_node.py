import comfy.utils
from ...engines.inworld_tts import inworld_tts, InworldTTSInput, validate_text, truncate_text


class InworldTTSNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "Hello, this is a test of the Inworld TTS API."}),
                "model_id": ("STRING", {"default": "inworld-tts-1"}),
                "voice_id": ("STRING", {"default": "Ashley"}),
                "api_base": ("STRING", {"default": "https://api.inworld.ai"}),
                "api_key": ("STRING", {"default": ""}),
            },
            "optional": {
                "auto_truncate": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("audio",)
    FUNCTION = "run"
    TITLE = "Inworld TTS"

    CATEGORY = "Inworld/TTS"
    DESCRIPTION = "Generate speech using Inworld TTS API"

    def __init__(self):
        pass

    def run(self, **kwargs):
        text = kwargs["text"]
        model_id = kwargs["model_id"]
        voice_id = kwargs["voice_id"]
        api_base = kwargs["api_base"]
        api_key = kwargs["api_key"]
        auto_truncate = kwargs.get("auto_truncate", True)
        
        # Validate and process text
        if not validate_text(text):
            if auto_truncate:
                text = truncate_text(text)
                print(f"Text was truncated to fit length limits: {len(text)} characters")
            else:
                print("Error: Invalid or too long text input")
                return (None,)
        
        # Create progress bar
        self.pbar = comfy.utils.ProgressBar(1)
        
        try:
            # Create input for TTS API
            tts_input = InworldTTSInput(
                text=text,
                voice_id=voice_id,
                model_id=model_id,
                api_base=api_base,
                api_key=api_key
            )
            
            # Generate audio
            self.pbar.update(1)
            result = inworld_tts(tts_input)
            
            print(f"Generated audio: {len(result.audio_content)} bytes")
            
            # Return audio bytes
            return (result.audio_content,)
            
        except Exception as e:
            print(f"Error in Inworld TTS: {str(e)}")
            return (None,)

    def update(self):
        self.pbar.update(1) 