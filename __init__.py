from .components.inworld_nodes.inworld_tts_node import InworldTTSNode
from .components.inworld_nodes.audio_save_node import InworldAudioSaveNode
from .components.inworld_nodes.audio_preview_node import InworldAudioPreviewNode

NODE_CLASS_MAPPINGS = {
    "InworldTTSNode": InworldTTSNode,
    "InworldAudioSaveNode": InworldAudioSaveNode,
    "InworldAudioPreviewNode": InworldAudioPreviewNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "InworldTTSNode": "Inworld TTS",
    "InworldAudioSaveNode": "Inworld Audio Save",
    "InworldAudioPreviewNode": "Inworld Audio Preview",
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]