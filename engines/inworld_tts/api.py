"""
Inworld TTS API module

This module provides the core functionality for interacting with the Inworld TTS API.
"""

import requests
import base64
import os
from typing import Optional
from pydantic import BaseModel


class InworldAPIConfig(BaseModel):
    """Configuration for Inworld API"""
    api_base: Optional[str] = None
    api_key: Optional[str] = None


class InworldTTSInput(InworldAPIConfig):
    """Input parameters for Inworld TTS"""
    text: str
    voice_id: str
    model_id: str


class InworldTTSOutput(BaseModel):
    """Output from Inworld TTS API"""
    audio_content: bytes


def inworld_tts(tts_input: InworldTTSInput) -> InworldTTSOutput:
    """
    Generate speech using Inworld TTS API
    
    Args:
        tts_input: Input parameters for TTS generation
        
    Returns:
        InworldTTSOutput containing the generated audio bytes
        
    Raises:
        ValueError: If API key is not provided
        Exception: If API request fails or response format is unexpected
    """
    api_base = tts_input.api_base or "https://api.inworld.ai"
    url = f"{api_base}/tts/v1/voice"

    api_key = tts_input.api_key or os.getenv("INWORLD_API_KEY")
    
    if not api_key:
        raise ValueError("API key is required. Set it in the node or as INWORLD_API_KEY environment variable.")

    headers = {
        "Authorization": f"Basic {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "text": tts_input.text,
        "voiceId": tts_input.voice_id,
        "modelId": tts_input.model_id,
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        audio_content = base64.b64decode(result["audioContent"])

        return InworldTTSOutput(audio_content=audio_content)
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")
    except KeyError as e:
        raise Exception(f"Unexpected API response format: {str(e)}")
    except Exception as e:
        raise Exception(f"Error processing TTS request: {str(e)}") 