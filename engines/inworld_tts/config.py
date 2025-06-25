"""
Configuration module for Inworld TTS

This module contains configuration constants and settings for the Inworld TTS engine.
"""

from typing import Dict, List

# Default API settings
DEFAULT_API_BASE = "https://api.inworld.ai"
DEFAULT_MODEL_ID = "inworld-tts-1"
DEFAULT_VOICE_ID = "Ashley"

# API endpoints
ENDPOINTS = {
    "tts": "/tts/v1/voice",
    "voices": "/tts/v1/voices",
    "models": "/tts/v1/models"
}

# Available voice IDs (common ones)
VOICE_IDS = [
    "Ashley",
    "Brian", 
    "Emma",
    "James",
    "Lisa",
    "Mark",
    "Sarah",
    "Michael",
    "Jessica",
    "Daniel"
]

# Available model IDs
MODEL_IDS = [
    "inworld-tts-1",
    "inworld-tts-premium"
]

# Request configuration
REQUEST_TIMEOUT = 30  # seconds
MAX_TEXT_LENGTH = 5000  # characters
SUPPORTED_AUDIO_FORMATS = ["wav", "mp3", "ogg"]

# Rate limiting (requests per minute)
RATE_LIMIT_RPM = 60

def get_voice_options() -> List[str]:
    """Get list of available voice options"""
    return VOICE_IDS.copy()

def get_model_options() -> List[str]:
    """Get list of available model options"""
    return MODEL_IDS.copy()

def get_endpoint_url(api_base: str, endpoint_key: str) -> str:
    """
    Get full endpoint URL
    
    Args:
        api_base: Base API URL
        endpoint_key: Key from ENDPOINTS dict
        
    Returns:
        Full endpoint URL
    """
    return f"{api_base.rstrip('/')}{ENDPOINTS[endpoint_key]}" 