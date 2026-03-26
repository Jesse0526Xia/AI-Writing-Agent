"""
创意写作 AI Agent
包含故事生成、角色管理、情节设计、风格控制、情感管理、伏笔系统等功能
v2.0 - 增加自然语言增强，消除AI机械化表达
"""

__version__ = "2.0.0"
__author__ = "Creative Writing AI"

# 核心模块
from .story_engine import StoryEngine
from .character_manager import CharacterManager
from .plot_generator import PlotGenerator
from .style_controller import StyleController
from .emotion_manager import EmotionManager
from .foreshadowing_system import ForeshadowingSystem
from .creative_agent import CreativeWritingAgent

# 增强模块（v2.0新增）
from .natural_language_enhancer import (
    NaturalLanguageEnhancer,
    EmotionNuance,
    EmotionBlender,
    naturalize,
    describe_emotion_naturally
)
from .enhanced_dialogue_system import (
    EnhancedDialogueGenerator,
    CharacterVoiceFingerprint,
    DialogueContext,
    DialogueStyle,
    create_character_voice,
    generate_natural_dialogue
)
from .literary_techniques import (
    MetaphorGenerator,
    RhetoricalDeviceGenerator,
    SensoryDescriptionEnhancer,
    LiteraryTechniquesIntegrator,
    add_metaphor,
    enhance_description,
    apply_literary_techniques
)
from .context_coherence import (
    ContextTracker,
    CoherenceAnalyzer,
    CoherenceManager,
    NarrativeCoherence,
    analyze_text_coherence,
    improve_text_coherence
)

__all__ = [
    # 核心模块
    "StoryEngine",
    "CharacterManager",
    "PlotGenerator",
    "StyleController",
    "EmotionManager",
    "ForeshadowingSystem",
    "CreativeWritingAgent",

    # 增强模块
    "NaturalLanguageEnhancer",
    "EmotionNuance",
    "EmotionBlender",
    "EnhancedDialogueGenerator",
    "CharacterVoiceFingerprint",
    "DialogueContext",
    "DialogueStyle",
    "MetaphorGenerator",
    "RhetoricalDeviceGenerator",
    "SensoryDescriptionEnhancer",
    "LiteraryTechniquesIntegrator",
    "ContextTracker",
    "CoherenceAnalyzer",
    "CoherenceManager",
    "NarrativeCoherence",

    # 便捷函数
    "naturalize",
    "describe_emotion_naturally",
    "create_character_voice",
    "generate_natural_dialogue",
    "add_metaphor",
    "enhance_description",
    "apply_literary_techniques",
    "analyze_text_coherence",
    "improve_text_coherence",
]
