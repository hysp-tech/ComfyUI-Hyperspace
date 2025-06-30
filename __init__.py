from .components.inworld_nodes.inworld_tts_node import InworldTTSNode
from .components.inworld_nodes.audio_save_node import InworldAudioSaveNode
from .components.inworld_nodes.audio_preview_node import InworldAudioPreviewNode

NODE_CLASS_MAPPINGS = {
    "InworldTTSNode": InworldTTSNode,
    "InworldAudioSaveNode": InworldAudioSaveNode,
    "InworldAudioPreviewNode": InworldAudioPreviewNode,
}