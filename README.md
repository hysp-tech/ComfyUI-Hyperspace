# ComfyUI-Hyperspace
Comfy Hyperspace Plugins

## Project Structure

```
ComfyUI-Hyperspace/
├── engines/                    # Core engines and utilities
│   └── inworld_tts/           # Inworld TTS engine
│       ├── __init__.py        # Package exports
│       ├── api.py             # Core API functionality
│       ├── config.py          # Configuration and constants
│       └── utils.py           # Utility functions
├── components/                 # ComfyUI custom nodes
│   └── inworld_nodes/         # Inworld TTS nodes
│       ├── inworld_tts_node.py
│       ├── audio_save_node.py
│       └── audio_preview_node.py
├── nodes.py                   # Node registry
└── test_inworld_tts.py       # Test script
```

## Features

### Engines
- **Modular design**: Engines are separate from ComfyUI nodes for better maintainability
- **Extensible structure**: Easy to add new TTS providers or engines
- **Rich utilities**: Text validation, audio analysis, file management
- **Configuration management**: Centralized settings and constants

### Nodes
- **Enhanced validation**: Automatic text length validation and truncation
- **Detailed audio info**: Sample rate, channels, duration analysis
- **Smart file handling**: Format validation and error handling
- **Progress feedback**: Real-time progress bars and detailed logging

## Inworld TTS Nodes

This plugin provides three custom nodes for integrating Inworld TTS (Text-to-Speech) API with ComfyUI:

### 1. Inworld TTS Node
Generates speech audio from text using the Inworld TTS API with enhanced validation.

**Node ID:** `InworldTTSNode`

**Inputs:**
- `text` (STRING): The text to convert to speech
- `model_id` (STRING): The TTS model ID (default: "inworld-tts-1")
- `voice_id` (STRING): The voice ID to use (default: "Ashley")
- `api_base` (STRING): The Inworld API base URL (default: "https://api.inworld.ai")
- `api_key` (STRING): Your Inworld API key
- `auto_truncate` (BOOLEAN, optional): Automatically truncate long text (default: True)

**Outputs:**
- `audio` (AUDIO): The generated audio bytes

**Features:**
- Automatic text validation and truncation
- Smart sentence boundary detection for truncation
- Detailed error reporting and logging

### 2. Inworld Audio Save Node
Saves audio bytes to a file with validation and detailed information.

**Node ID:** `InworldAudioSaveNode`

**Inputs:**
- `audio` (AUDIO): The audio bytes to save
- `filename` (STRING): The filename to save as (default: "output.wav")
- `output_dir` (STRING): The output directory (default: "outputs")
- `show_info` (BOOLEAN, optional): Show detailed audio information (default: True)

**Outputs:**
- `file_path` (STRING): The path where the file was saved

**Features:**
- Audio format validation
- Detailed audio analysis (sample rate, channels, duration)
- Automatic directory creation
- Comprehensive error handling

### 3. Inworld Audio Preview Node
Preview audio bytes with detailed technical information.

**Node ID:** `InworldAudioPreviewNode`

**Inputs:**
- `audio` (AUDIO): The audio bytes to preview
- `show_info` (BOOLEAN, optional): Show detailed audio information (default: True)

**Outputs:**
- `audio` (AUDIO): The same audio bytes (pass-through for preview)

**Features:**
- Detailed audio analysis and reporting
- Format detection (mono/stereo)
- Technical specifications display

## Setup

1. Install the required dependencies:
```bash
pip install pydantic requests
```

2. Set your Inworld API key either:
   - In the node's `api_key` input field
   - As an environment variable: `INWORLD_API_KEY`

## Usage

1. Add the "Inworld TTS" node to your workflow
2. Configure the text, model, voice, and API settings
3. Connect the audio output to either:
   - "Inworld Audio Save" node to save to file
   - "Inworld Audio Preview" node to preview in ComfyUI
   - Or both!

## Example Workflow

```
Text Input → Inworld TTS → Audio Save
                 ↓
           Audio Preview
```

## Testing

Run the test script to verify the API integration:

```bash
export INWORLD_API_KEY="your_api_key_here"
python test_inworld_tts.py
```

The test script will:
- Generate a test audio file
- Display detailed audio information
- Save the output to `test_outputs/test_output.wav`

## Available Voices

The Inworld TTS API supports various voices. Some common voice IDs include:
- Ashley
- Brian
- Emma
- James
- Lisa
- Mark
- Sarah
- Michael
- Jessica
- Daniel

Check the Inworld documentation for the complete list of available voices.

## Engine Utilities

The `engines.inworld_tts` package provides several utility functions:

### Text Processing
- `validate_text()`: Validate input text
- `truncate_text()`: Smart text truncation with sentence boundaries

### Audio Analysis
- `get_audio_info()`: Extract sample rate, channels, and duration
- `validate_audio_format()`: Check if audio format is supported

### File Management
- `save_audio_file()`: Save audio with proper error handling
- `get_file_extension()`: Extract file extensions

### Configuration
- Pre-defined voice and model lists
- Configurable API endpoints and settings
- Rate limiting and timeout configurations
