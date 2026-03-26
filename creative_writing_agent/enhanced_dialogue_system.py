"""
增强对话生成系统
消除机械化对话，让每个角色都有独特的语言风格
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
import random


class DialogueStyle(Enum):
    """对话风格"""
    FORMAL = "formal"  # 正式
    CASUAL = "casual"  # 随意
    AGGRESSIVE = "aggressive"  - 激进
    TENTATIVE = "tentative"  - 犹豫
    WITTY = "witty"  - 机智
    SARCASTIC = "sarcastic"  - 讽刺
    POETIC = "poetic"  - 诗意
    BLUNT = "blunt"  - 直率
    ELOQUENT = "eloquent"  - 雄辩
    HUMBLE = "humble"  - 谦逊


class CharacterVoiceFingerprint:
    """角色语言指纹"""

    def __init__(
        self,
        sentence_length_preference: str = "medium",
        vocabulary_level: str = "moderate",
        use_slang: bool = False,
        specific_phrases: Optional[List[str]] = None,
        sentence_structure: str = "standard",
        tone_markers: Optional[Dict[str, List[str]]] = None,
        pause_patterns: Optional[List[str]] = None,
        repetition_tendencies: Optional[List[str]] = None,
        speech_rate: str = "normal",
        emotional_expression: str = "moderate"
    ):
        """
        初始化角色语言指纹

        Args:
            sentence_length_preference: 句长偏好 (short/medium/long)
            vocabulary_level: 词汇水平 (simple/moderate/complex)
            use_slang: 是否使用俚语
            specific_phrases: 特定口头禅
            sentence_structure: 句式结构 (simple/complex/fragmented)
            tone_markers: 语调标记
            pause_patterns: 停顿模式
            repetition_tendencies: 重复倾向
            speech_rate: 语速 (slow/normal/fast)
            emotional_expression: 情感表达 (subtle/moderate/intense)
        """
        self.sentence_length_preference = sentence_length_preference
        self.vocabulary_level = vocabulary_level
        self.use_slang = use_slang
        self.specific_phrases = specific_phrases or []
        self.sentence_structure = sentence_structure
        self.tone_markers = tone_markers or self._default_tone_markers()
        self.pause_patterns = pause_patterns or []
        self.repetition_tendencies = repetition_tendencies or []
        self.speech_rate = speech_rate
        self.emotional_expression = emotional_expression

    def _default_tone_markers(self) -> Dict[str, List[str]]:
        """默认语调标记"""
        return {
            "formal": ["您", "请", "麻烦", "劳驾"],
            "casual": ["嗯", "啊", "那个", "呃"],
            "aggressive": ["哼", "切", "啧", "废话"],
            "tentative": ["可能", "也许", "大概", "好像"],
            "witty": ["哈哈", "有趣", "妙极了", "有意思"],
            "sarcastic": ["呵", "真是", "了不起", "厉害"],
            "poetic": ["仿佛", "宛如", "似乎", "犹如"],
            "blunt": ["直说吧", "老实说", "不管怎样", "总之"],
            "eloquent": ["诚然", "毋庸置疑", "显而易见", "毋庸置疑"],
            "humble": ["不敢当", "惭愧", "哪里哪里", "过奖"]
        }

    def add_phrase(self, phrase: str):
        """添加口头禅"""
        if phrase not in self.specific_phrases:
            self.specific_phrases.append(phrase)

    def get_tone_marker(self, style: DialogueStyle) -> Optional[str]:
        """获取语调标记"""
        if style.value in self.tone_markers:
            markers = self.tone_markers[style.value]
            return random.choice(markers) if markers else None
        return None


class DialogueContext:
    """对话语境"""

    def __init__(
        self,
        characters: List[str],
        situation: str,
        relationship: str,
        location: Optional[str] = None,
        time: Optional[str] = None,
        urgency: str = "normal",
        intimacy: str = "moderate",
        topic: Optional[str] = None
    ):
        """
        初始化对话语境

        Args:
            characters: 参与对话的角色
            situation: 情境
            relationship: 角色关系
            location: 地点
            time: 时间
            urgency: 紧急程度 (low/normal/high)
            intimacy: 亲密程度 (low/moderate/high)
            topic: 话题
        """
        self.characters = characters
        self.situation = situation
        self.relationship = relationship
        self.location = location
        self.time = time
        self.urgency = urgency
        self.intimacy = intimacy
        self.topic = topic

    def analyze(self) -> Dict:
        """分析语境"""
        return {
            "formality_level": self._calculate_formality(),
            "emotional_tone": self._determine_emotional_tone(),
            "urgency": self.urgency,
            "intimacy": self.intimacy,
            "topic_relevance": self._assess_topic_relevance()
        }

    def _calculate_formality(self) -> str:
        """计算正式程度"""
        if self.intimacy == "high" and self.urgency == "low":
            return "casual"
        elif self.urgency == "high":
            return "direct"
        elif self.relationship in ["陌生人", "上下级"]:
            return "formal"
        else:
            return "moderate"

    def _determine_emotional_tone(self) -> str:
        """确定情感基调"""
        if "紧急" in self.situation or "危险" in self.situation:
            return "tense"
        elif "轻松" in self.situation or "愉快" in self.situation:
            return "relaxed"
        elif "悲伤" in self.situation or "痛苦" in self.situation:
            return "somber"
        else:
            return "neutral"

    def _assess_topic_relevance(self) -> str:
        """评估话题相关性"""
        return "relevant" if self.topic else "general"


class NaturalDialogueFeatures:
    """自然对话特征"""

    @staticmethod
    def add_interruption(dialogue: str, probability: float = 0.1) -> str:
        """添加打断"""
        if random.random() < probability:
            interruption_markers = ["——", "...", "——", "等等"]
            marker = random.choice(interruption_markers)
            # 在对话中间插入打断
            words = dialogue.split()
            if len(words) > 2:
                insert_pos = random.randint(1, len(words) - 1)
                words.insert(insert_pos, marker)
                return " ".join(words)
        return dialogue

    @staticmethod
    def add_hesitation(dialogue: str, probability: float = 0.15) -> str:
        """添加犹豫"""
        if random.random() < probability:
            hesitation_markers = ["呃...", "嗯...", "那个...", "这个..."]
            marker = random.choice(hesitation_markers)
            # 在句首添加犹豫
            return f"{marker}{dialogue}"
        return dialogue

    @staticmethod
    def add_filler(dialogue: str, probability: float = 0.2) -> str:
        """添加填充词"""
        if random.random() < probability:
            filler_words = ["就是", "就是说", "其实", "反正"]
            filler = random.choice(filler_words)
            # 在对话中随机位置添加
            words = dialogue.split()
            if len(words) > 1:
                insert_pos = random.randint(1, len(words))
                words.insert(insert_pos, filler)
                return " ".join(words)
        return dialogue

    @staticmethod
    def add_correction(dialogue: str, probability: float = 0.1) -> str:
        """添加自我纠正"""
        if random.random() < probability:
            # 简单实现：重复最后一个词
            words = dialogue.split()
            if len(words) > 0:
                last_word = words[-1]
                return f"{dialogue}，我是说{last_word}"
        return dialogue

    @staticmethod
    def add_incomplete_sentence(dialogue: str, probability: float = 0.05) -> str:
        """添加不完整句子"""
        if random.random() < probability:
            # 简单实现：截断句子
            words = dialogue.split()
            if len(words) > 3:
                cut_pos = random.randint(len(words) // 2, len(words) - 1)
                return " ".join(words[:cut_pos]) + "..."
        return dialogue

    @staticmethod
    def add_repetition(dialogue: str, probability: float = 0.1) -> str:
        """添加重复"""
        if random.random() < probability:
            words = dialogue.split()
            if len(words) > 2:
                # 重复第一个词
                return f"{words[0]}... {dialogue}"
        return dialogue


class EnhancedDialogueGenerator:
    """增强对话生成器"""

    def __init__(self, llm_client=None):
        self.llm_client = llm_client
        self.character_voices: Dict[str, CharacterVoiceFingerprint] = {}
        self.natural_features = NaturalDialogueFeatures()

        # 对话风格模板
        self.style_templates = {
            DialogueStyle.FORMAL: {
                "vocabulary": ["请", "您", "劳驾", "麻烦", "感谢"],
                "sentence_structure": "complete",
                "tone": "polite"
            },
            DialogueStyle.CASUAL: {
                "vocabulary": ["嗯", "啊", "那个", "哎", "哦"],
                "sentence_structure": "relaxed",
                "tone": "friendly"
            },
            DialogueStyle.AGGRESSIVE: {
                "vocabulary": ["哼", "切", "废话", "少废话", "滚"],
                "sentence_structure": "direct",
                "tone": "hostile"
            },
            DialogueStyle.TENTATIVE: {
                "vocabulary": ["可能", "也许", "大概", "好像", "似乎"],
                "sentence_structure": "hesitant",
                "tone": "uncertain"
            },
            DialogueStyle.WITTY: {
                "vocabulary": ["哈哈", "有趣", "妙", "有意思", "好玩"],
                "sentence_structure": "clever",
                "tone": "playful"
            },
            DialogueStyle.SARCASTIC: {
                "vocabulary": ["呵", "真是", "了不起", "厉害", "佩服"],
                "sentence_structure": "ironic",
                "tone": "mocking"
            },
            DialogueStyle.POETIC: {
                "vocabulary": ["仿佛", "宛如", "似乎", "犹如", "恰似"],
                "sentence_structure": "flowery",
                "tone": "elegant"
            },
            DialogueStyle.BLUNT: {
                "vocabulary": ["直说吧", "老实说", "不管怎样", "总之", "说真的"],
                "sentence_structure": "direct",
                "tone": "frank"
            },
            DialogueStyle.ELOQUENT: {
                "vocabulary": ["诚然", "毋庸置疑", "显而易见", "毋庸置疑", "显然"],
                "sentence_structure": "sophisticated",
                "tone": "articulate"
            },
            DialogueStyle.HUMBLE: {
                "vocabulary": ["不敢当", "惭愧", "哪里哪里", "过奖", "不敢"],
                "sentence_structure": "modest",
                "tone": "deferential"
            }
        }

    def register_character_voice(
        self,
        character_name: str,
        voice_fingerprint: Optional[CharacterVoiceFingerprint] = None,
        **kwargs
    ):
        """
        注册角色语言指纹

        Args:
            character_name: 角色名
            voice_fingerprint: 语言指纹（可选）
            **kwargs: 直接创建指纹的参数
        """
        if voice_fingerprint:
            self.character_voices[character_name] = voice_fingerprint
        else:
            self.character_voices[character_name] = CharacterVoiceFingerprint(**kwargs)

    def generate_dialogue(
        self,
        character_name: str,
        base_message: str,
        context: Optional[DialogueContext] = None,
        llm_generate_func: Optional[callable] = None
    ) -> str:
        """
        生成对话

        Args:
            character_name: 角色名
            base_message: 基础消息
            context: 对话语境
            llm_generate_func: LLM 生成函数（可选）

        Returns:
            生成的对话
        """
        # 步骤1: 应用角色语言指纹
        dialogue = self._apply_character_voice(character_name, base_message)

        # 步骤2: 根据语境调整
        if context:
            dialogue = self._adapt_to_context(dialogue, context)

        # 步骤3: 添加自然对话特征
        dialogue = self._add_natural_features(dialogue)

        # 步骤4: 如果有 LLM，进行最终优化
        if llm_generate_func:
            dialogue = self._llm_optimize(dialogue, character_name, context)

        return dialogue

    def _apply_character_voice(self, character_name: str, message: str) -> str:
        """应用角色语言指纹"""
        voice = self.character_voices.get(character_name)
        if not voice:
            return message

        result = message

        # 添加口头禅
        if voice.specific_phrases and random.random() < 0.3:
            phrase = random.choice(voice.specific_phrases)
            if random.random() < 0.5:
                result = f"{phrase}，{result}"
            else:
                result = f"{result}{phrase}"

        # 根据句长偏好调整
        if voice.sentence_length_preference == "short":
            # 简化长句
            result = self._simplify_sentences(result)
        elif voice.sentence_length_preference == "long":
            # 扩展短句
            result = self._expand_sentences(result)

        return result

    def _adapt_to_context(self, dialogue: str, context: DialogueContext) -> str:
        """根据语境调整对话"""
        context_analysis = context.analyze()

        result = dialogue

        # 根据正式程度调整
        if context_analysis["formality_level"] == "formal":
            # 添加礼貌用语
            polite_markers = ["请", "您", "劳驾"]
            if random.random() < 0.3:
                marker = random.choice(polite_markers)
                result = f"{marker}，{result}"
        elif context_analysis["formality_level"] == "casual":
            # 添加随意用语
            casual_markers = ["嗯", "啊", "那个"]
            if random.random() < 0.3:
                marker = random.choice(casual_markers)
                result = f"{marker}，{result}"

        # 根据紧急程度调整
        if context_analysis["urgency"] == "high":
            # 减少犹豫和停顿
            result = result.replace("呃...", "").replace("嗯...", "")
            # 使用更直接的表达
            result = result.replace("可能", "").replace("也许", "")

        return result

    def _add_natural_features(self, dialogue: str) -> str:
        """添加自然对话特征"""
        result = dialogue

        # 按顺序添加各种自然特征
        result = self.natural_features.add_hesitation(result)
        result = self.natural_features.add_filler(result)
        result = self.natural_features.add_correction(result)
        result = self.natural_features.add_interruption(result)
        result = self.natural_features.add_repetition(result)
        result = self.natural_features.add_incomplete_sentence(result)

        return result

    def _llm_optimize(
        self,
        dialogue: str,
        character_name: str,
        context: Optional[DialogueContext]
    ) -> str:
        """使用 LLM 优化对话"""
        if not self.llm_client:
            return dialogue

        voice = self.character_voices.get(character_name)
        voice_description = ""
        if voice:
            voice_description = f"""
            语言特征：
            - 句长偏好：{voice.sentence_length_preference}
            - 词汇水平：{voice.vocabulary_level}
            - 口头禅：{', '.join(voice.specific_phrases[:3])}
            """

        context_description = ""
        if context:
            context_description = f"""
            语境：
            - 情境：{context.situation}
            - 关系：{context.relationship}
            - 紧急程度：{context.urgency}
            """

        prompt = f"""
        原始对话：{dialogue}
        角色：{character_name}
        {voice_description}
        {context_description}

        请将这段对话重写，使其：
        1. 符合角色的语言特征
        2. 自然流畅，避免机械化
        3. 适应对话语境
        4. 保持原意不变

        优化后的对话：
        """

        try:
            return self.llm_client.generate(prompt)
        except:
            return dialogue

    def _simplify_sentences(self, text: str) -> str:
        """简化句子"""
        # 简化实现：按句号分割并选择较短的部分
        sentences = text.split("。")
        simplified = []
        for sentence in sentences:
            if sentence.strip():
                words = sentence.split()
                if len(words) > 10:
                    # 截取前半部分
                    simplified.append(" ".join(words[:len(words)//2]) + "。")
                else:
                    simplified.append(sentence + "。")
        return "".join(simplified)

    def _expand_sentences(self, text: str) -> str:
        """扩展句子"""
        # 简化实现：添加一些修饰词
        modifiers = ["非常", "特别", "相当", "十分", "极其"]
        result = text
        for modifier in modifiers:
            if modifier not in result and random.random() < 0.3:
                result = result.replace("是", f"是{modifier}", 1)
                break
        return result

    def generate_conversation(
        self,
        script: List[Dict],
        context: Optional[DialogueContext] = None,
        llm_generate_func: Optional[callable] = None
    ) -> List[str]:
        """
        生成完整的对话

        Args:
            script: 对话脚本，每个元素包含 {character, message}
            context: 对话语境
            llm_generate_func: LLM 生成函数（可选）

        Returns:
            对话列表
        """
        conversation = []

        for line in script:
            character = line["character"]
            message = line["message"]

            dialogue = self.generate_dialogue(
                character_name=character,
                base_message=message,
                context=context,
                llm_generate_func=llm_generate_func
            )

            conversation.append(f"{character}：{dialogue}")

        return conversation


# 便捷函数
def create_character_voice(
    sentence_length: str = "medium",
    vocabulary_level: str = "moderate",
    **kwargs
) -> CharacterVoiceFingerprint:
    """快速创建角色语言指纹"""
    return CharacterVoiceFingerprint(
        sentence_length_preference=sentence_length,
        vocabulary_level=vocabulary_level,
        **kwargs
    )


def generate_natural_dialogue(
    character: str,
    message: str,
    style: str = "casual"
) -> str:
    """快速生成自然对话"""
    generator = EnhancedDialogueGenerator()
    generator.register_character_voice(
        character,
        sentence_length_preference="medium",
        vocabulary_level="moderate"
    )
    return generator.generate_dialogue(character, message)
