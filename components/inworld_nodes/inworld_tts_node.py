import comfy.utils
from ...engines.inworld_tts import (
    inworld_tts,
    InworldTTSInput,
    validate_text,
    truncate_text,
)
import tempfile
import torchaudio
import os


class InworldTTSNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "Hello, this is a test of the Inworld TTS API.",
                    },
                ),
                "model_id": ("STRING", {"default": "inworld-tts-1"}),
                "voice_id": ("STRING", {"default": "Ashley"}),
                "api_base": ("STRING", {"default": "https://api.inworld.ai"}),
                "api_key": ("STRING", {"default": ""}),
            },
            "optional": {
                "auto_truncate": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("audio",)
    FUNCTION = "run"
    TITLE = "Inworld TTS"

    CATEGORY = "Inworld"
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
                print(
                    f"Text was truncated to fit length limits: {len(text)} characters"
                )
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
                api_key=api_key,
            )

            # Generate audio
            self.pbar.update(1)
            result = inworld_tts(tts_input)

            print(f"Generated audio: {len(result.audio_content)} bytes")

            # Save audio to file
            # 1. Save audio bytes to temporary file
            # Inworld API returns WAV format, so we use .wav extension
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
                temp_file.write(result.audio_content)
                temp_filepath = temp_file.name

            # 2. Load audio file using torchaudio
            try:
                waveform, sample_rate = torchaudio.load(temp_filepath)
            finally:
                # 3. Delete temporary file
                os.remove(temp_filepath)

            # 4. Wrap audio data in ComfyUI's AUDIO format and return
            # waveform shape is usually [channels, num_samples], we need to add a batch dimension
            audio_dict = {"waveform": waveform.unsqueeze(0), "sample_rate": sample_rate}
            self.pbar.update(1)
            return (audio_dict,)

        except Exception as e:
            print(f"Error in Inworld TTS: {str(e)}")
            return (None,)

    def update(self):
        self.pbar.update(1)
