"""
Utilities module for Inworld TTS

This module contains utility functions for the Inworld TTS engine.
"""

import os
import wave
import io
from typing import Optional, Tuple
from .config import MAX_TEXT_LENGTH, SUPPORTED_AUDIO_FORMATS


def validate_text(text: str) -> bool:
    """
    Validate input text for TTS
    
    Args:
        text: Text to validate
        
    Returns:
        True if text is valid, False otherwise
    """
    if not text or not text.strip():
        return False
    
    if len(text) > MAX_TEXT_LENGTH:
        return False
        
    return True


def truncate_text(text: str, max_length: Optional[int] = None) -> str:
    """
    Truncate text to maximum length
    
    Args:
        text: Text to truncate
        max_length: Maximum length (defaults to MAX_TEXT_LENGTH)
        
    Returns:
        Truncated text
    """
    max_len = max_length or MAX_TEXT_LENGTH
    if len(text) <= max_len:
        return text
    
    # Try to truncate at sentence boundary
    truncated = text[:max_len]
    last_period = truncated.rfind('.')
    last_exclamation = truncated.rfind('!')
    last_question = truncated.rfind('?')
    
    last_sentence_end = max(last_period, last_exclamation, last_question)
    
    if last_sentence_end > max_len * 0.8:  # If we found a sentence end in the last 20%
        return truncated[:last_sentence_end + 1]
    else:
        return truncated


def get_audio_info(audio_bytes: bytes) -> Tuple[Optional[int], Optional[int], Optional[float]]:
    """
    Get basic information about audio bytes (assuming WAV format)
    
    Args:
        audio_bytes: Audio data in bytes
        
    Returns:
        Tuple of (sample_rate, channels, duration_seconds) or (None, None, None) if unable to parse
    """
    try:
        with wave.open(io.BytesIO(audio_bytes), 'rb') as wav_file:
            sample_rate = wav_file.getframerate()
            channels = wav_file.getnchannels()
            frames = wav_file.getnframes()
            duration = frames / sample_rate if sample_rate > 0 else 0
            return sample_rate, channels, duration
    except Exception:
        return None, None, None


def save_audio_file(audio_bytes: bytes, filename: str, output_dir: str = "outputs") -> str:
    """
    Save audio bytes to a file
    
    Args:
        audio_bytes: Audio data in bytes
        filename: Name of the file to save
        output_dir: Directory to save the file in
        
    Returns:
        Full path of the saved file
        
    Raises:
        OSError: If unable to create directory or save file
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create full file path
    file_path = os.path.join(output_dir, filename)
    
    # Write audio bytes to file
    with open(file_path, 'wb') as f:
        f.write(audio_bytes)
    
    return file_path


def get_file_extension(filename: str) -> Optional[str]:
    """
    Get file extension from filename
    
    Args:
        filename: Name of the file
        
    Returns:
        File extension without dot, or None if no extension
    """
    if '.' not in filename:
        return None
    
    return filename.split('.')[-1].lower()


def validate_audio_format(filename: str) -> bool:
    """
    Validate if the audio format is supported
    
    Args:
        filename: Name of the file
        
    Returns:
        True if format is supported, False otherwise
    """
    ext = get_file_extension(filename)
    return ext in SUPPORTED_AUDIO_FORMATS if ext else False 