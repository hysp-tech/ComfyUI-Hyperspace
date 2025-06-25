#!/usr/bin/env python3
"""
Test script for Inworld TTS API functionality
"""

import os
import sys
from engines.inworld_tts import inworld_tts, InworldTTSInput, get_audio_info, save_audio_file

def test_tts():
    """Test the TTS functionality"""
    
    # Check if API key is available
    api_key = os.getenv("INWORLD_API_KEY")
    if not api_key:
        print("Please set INWORLD_API_KEY environment variable")
        return False
    
    try:
        # Create test input
        tts_input = InworldTTSInput(
            text="Hello, this is a test of the Inworld TTS API!",
            voice_id="Ashley",
            model_id="inworld-tts-1",
            api_key=api_key
        )
        
        print("Testing Inworld TTS API...")
        result = inworld_tts(tts_input)
        
        print(f"Success! Generated audio with {len(result.audio_content)} bytes")
        
        # Get audio info
        sample_rate, channels, duration = get_audio_info(result.audio_content)
        if sample_rate:
            print(f"Audio info:")
            print(f"  Sample rate: {sample_rate} Hz")
            print(f"  Channels: {channels}")
            print(f"  Duration: {duration:.2f} seconds")
        
        # Save test audio using utility function
        file_path = save_audio_file(result.audio_content, "test_output.wav", "test_outputs")
        
        print(f"Audio saved to: {file_path}")
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_tts()
    sys.exit(0 if success else 1) 