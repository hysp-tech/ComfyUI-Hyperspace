"""
Inworld TTS Engine

This package provides utilities and classes for integrating with the Inworld TTS API.
"""

from .api import inworld_tts, InworldTTSInput, InworldTTSOutput, InworldAPIConfig
from .config import (
    DEFAULT_API_BASE,
    DEFAULT_MODEL_ID, 
    DEFAULT_VOICE_ID,
    VOICE_IDS,
    MODEL_IDS,
    get_voice_options,
    get_model_options
)
from .utils import (
    validate_text,
    truncate_text,
    get_audio_info,
    save_audio_file,
    validate_audio_format
)

__version__ = "0.1.0"

__all__ = [
    # Core API
    "inworld_tts",
    "InworldTTSInput", 
    "InworldTTSOutput",
    "InworldAPIConfig",
    # Configuration
    "DEFAULT_API_BASE",
    "DEFAULT_MODEL_ID",
    "DEFAULT_VOICE_ID", 
    "VOICE_IDS",
    "MODEL_IDS",
    "get_voice_options",
    "get_model_options",
    # Utilities
    "validate_text",
    "truncate_text",
    "get_audio_info",
    "save_audio_file",
    "validate_audio_format"
] 