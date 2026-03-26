"""
自然语言增强模块
消除AI机械化表达，提升文本自然度和文学性
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
import random


class EmotionIntensity(Enum):
    """情感强度 - 细化版本"""
    BARELY_PERCEPTIBLE = 1  # 几乎察觉不到
    SUBTLE = 2  # 微妙
    NOTICEABLE = 3  # 明显
    STRONG = 4  # 强烈
    OVERWHELMING = 5  # 压倒性的


class EmotionNuance:
    """情感细微差别"""

    # 细化情感分类（50+种）
    EMOTION_TAXONOMY = {
        "快乐": {
            "subtypes": [
                "喜悦", "兴奋", "满足", "得意", "狂喜",
                "欣慰", "陶醉", "欢愉", "雀跃", "欣喜",
                "愉悦", "快活", "舒畅", "畅快", "欢畅"
            ],
            "manifestations": {
                "轻微": ["嘴角微微上扬", "眼中闪过一丝笑意", "眉眼弯弯"],
                "轻度": ["轻声一笑", "脸上露出笑容", "心情轻快"],
                "中度": ["开怀大笑", "喜上眉梢", "满心欢喜"],
                "强烈": ["捧腹大笑", "欣喜若狂", "激动不已"],
                "极度": ["狂喜乱舞", "喜极而泣", "欣喜若狂到无法自持"]
            }
        },
        "悲伤": {
            "subtypes": [
                "忧伤", "悲痛", "哀伤", "凄凉", "绝望",
                "惆怅", "郁结", "哀愁", "悲凉", "心碎",
                "哀痛", "悲怆", "凄楚", "惨痛", "悲恸"
            ],
            "manifestations": {
                "轻微": ["眼眶微湿", "眉头轻蹙", "一声叹息"],
                "轻度": ["眼含泪光", "声音低沉", "神情黯然"],
                "中度": ["泪流满面", "心如刀割", "悲痛欲绝"],
                "强烈": ["痛哭失声", "肝肠寸断", "悲痛欲绝"],
                "极度": ["悲痛欲绝到无法呼吸", "心如死灰", "万念俱灰"]
            }
        },
        "愤怒": {
            "subtypes": [
                "恼怒", "愤慨", "暴怒", "震怒", "怒火中烧",
                "愤懑", "恼火", "气愤", "激愤", "愤怒不已"
            ],
            "manifestations": {
                "轻微": ["眉头紧锁", "握紧拳头", "呼吸急促"],
                "轻度": ["脸色阴沉", "声音提高", "怒目而视"],
                "中度": ["拍案而起", "怒不可遏", "火冒三丈"],
                "强烈": ["暴跳如雷", "怒发冲冠", "气得发抖"],
                "极度": ["怒不可遏到失去理智", "七窍生烟", "怒火攻心"]
            }
        },
        "恐惧": {
            "subtypes": [
                "惊恐", "害怕", "畏惧", "恐慌", "战栗",
                "胆怯", "惶恐", "惊骇", "畏惧", "心惊肉跳"
            ],
            "manifestations": {
                "轻微": ["心跳加速", "手心出汗", "眼神闪烁"],
                "轻度": ["声音颤抖", "后退半步", "呼吸紊乱"],
                "中度": ["浑身发抖", "脸色煞白", "语无伦次"],
                "强烈": ["惊恐万状", "魂飞魄散", "瑟瑟发抖"],
                "极度": ["恐惧到无法动弹", "魂不附体", "惊骇欲绝"]
            }
        },
        "惊讶": {
            "subtypes": [
                "惊奇", "惊诧", "错愕", "惊愕", "震惊",
                "诧异", "愕然", "惊异", "惊呆", "目瞪口呆"
            ],
            "manifestations": {
                "轻微": ["眉毛上扬", "眨眼", "停顿"],
                "轻度": ["张口结舌", "瞪大眼睛", "倒吸一口气"],
                "中度": ["难以置信", "目瞪口呆", "惊愕不已"],
                "强烈": ["震惊万分", "瞠目结舌", "惊得说不出话"],
                "极度": ["震惊到大脑空白", "惊骇欲绝", "惊得魂飞魄散"]
            }
        }
    }

    @classmethod
    def get_emotion_manifestation(cls, emotion: str, intensity: int) -> str:
        """获取情感表现形式"""
        intensity_map = {
            1: "轻微",
            2: "轻度",
            3: "中度",
            4: "强烈",
            5: "极度"
        }

        intensity_key = intensity_map.get(intensity, "中度")

        if emotion in cls.EMOTION_TAXONOMY:
            manifestations = cls.EMOTION_TAXONOMY[emotion]["manifestations"]
            if intensity_key in manifestations:
                return random.choice(manifestations[intensity_key])

        # 默认返回
        return f"感到{emotion}"


class EmotionBlender:
    """情感混合器 - 处理复杂情感"""

    def __init__(self):
        self.blend_patterns = {
            "冲突": ["既...又...", "一方面...另一方面...", "内心充满了...与..."],
            "过渡": ["从...逐渐转变为...", "...的情绪慢慢消退，取而代之的是..."],
            "叠加": ["在...的基础上，又添了一份...", "...之余，还夹杂着..."],
            "复杂": ["五味杂陈", "百感交集", "心绪纷乱"]
        }

    def blend_emotions(self, emotions: List[Tuple[str, float]]) -> Dict:
        """
        混合多种情感

        Args:
            emotions: 情感列表，每个元素为 (情感类型, 权重)

        Returns:
            混合后的情感描述
        """
        if not emotions:
            return {"description": ""}

        # 按权重排序
        sorted_emotions = sorted(emotions, key=lambda x: x[1], reverse=True)

        primary_emotion = sorted_emotions[0][0]
        secondary_emotions = sorted_emotions[1:]

        # 计算冲突程度
        conflict_level = self._calculate_conflict(sorted_emotions)

        # 生成描述
        description = self._generate_blend_description(
            primary_emotion,
            secondary_emotions,
            conflict_level
        )

        return {
            "primary_emotion": primary_emotion,
            "secondary_emotions": [e[0] for e in secondary_emotions],
            "conflict_level": conflict_level,
            "description": description
        }

    def _calculate_conflict(self, emotions: List[Tuple[str, float]]) -> float:
        """计算情感冲突程度"""
        # 这里可以定义哪些情感是冲突的
        conflicting_pairs = [
            ("快乐", "悲伤"),
            ("愤怒", "恐惧"),
            ("希望", "绝望")
        ]

        conflict_score = 0
        for i in range(len(emotions)):
            for j in range(i + 1, len(emotions)):
                if (emotions[i][0], emotions[j][0]) in conflicting_pairs or \
                   (emotions[j][0], emotions[i][0]) in conflicting_pairs:
                    conflict_score += emotions[i][1] * emotions[j][1]

        return min(1.0, conflict_score)

    def _generate_blend_description(
        self,
        primary_emotion: str,
        secondary_emotions: List[Tuple[str, float]],
        conflict_level: float
    ) -> str:
        """生成混合情感描述"""
        if not secondary_emotions:
            return EmotionNuance.get_emotion_manifestation(primary_emotion, 3)

        if conflict_level > 0.5:
            # 高冲突 - 使用冲突表达
            pattern = random.choice(self.blend_patterns["冲突"])
            desc = pattern.format(
                primary_emotion,
                secondary_emotions[0][0]
            )
            return f"{desc}，内心充满了矛盾"

        elif len(secondary_emotions) == 1:
            # 单一辅助情感
            pattern = random.choice(self.blend_patterns["叠加"])
            return pattern.format(primary_emotion, secondary_emotions[0][0])

        else:
            # 多种情感混合
            pattern = random.choice(self.blend_patterns["复杂"])
            return pattern


class NaturalLanguageEnhancer:
    """自然语言增强器"""

    def __init__(self, llm_client=None):
        self.llm_client = llm_client
        self.emotion_blender = EmotionBlender()

        # 机械化表达替换库
        self.mechanical_replacements = {
            "他感到很高兴": [
                "一股难以抑制的喜悦涌上心头",
                "他的嘴角不自觉地上扬",
                "心中涌起一阵暖流",
                "整个人都轻快了起来"
            ],
            "她决定采取行动": [
                "她下定决心，不再犹豫",
                "她深吸一口气，准备行动",
                "一个念头在她脑海中成形",
                "她握紧拳头，准备迈出这一步"
            ],
            "这是一个重要的转折": [
                "命运在此刻发生了改变",
                "一切都在这一刻发生了转折",
                "这个瞬间注定不平凡",
                "转折点悄然而至"
            ],
            "经过一番思考，他明白了": [
                "思索良久，他终于领悟了其中的真谛",
                "经过反复推敲，真相渐渐浮出水面",
                "在深思熟虑之后，他豁然开朗",
                "仔细琢磨之后，他终于明白了"
            ],
            "天气很好": [
                "阳光明媚，微风拂面",
                "天空湛蓝，万里无云",
                "阳光透过树叶洒下斑驳的光影",
                "空气中弥漫着清新的气息"
            ],
            "房间很乱": [
                "房间里一片狼藉，物品散落一地",
                "杂乱的物品堆满了整个空间",
                "房间里乱七八糟，无处下脚",
                "物品散乱地堆放着，显得格外凌乱"
            ],
            "他看起来很累": [
                "他的眼窝深陷，显露出深深的疲惫",
                "疲惫刻在他的脸上，连脚步都变得沉重",
                "他满身疲惫，仿佛连说话的力气都没有了",
                "疲惫像潮水一样淹没了他"
            ],
            "风景很美": [
                "眼前的美景如诗如画，令人陶醉",
                "大自然的美景让人流连忘返",
                "风景如画，美不胜收",
                "这景色美得让人屏住呼吸"
            ]
        }

        # 感官描写词库
        self.sensory_vocabulary = {
            "视觉": {
                "颜色": ["绯红", "苍白", "黯淡", "璀璨", "湛蓝", "翠绿", "金黄", "银白"],
                "光影": ["斑驳", "朦胧", "刺眼", "柔和", "昏暗", "明亮", "闪烁", "摇曳"],
                "动态": ["流淌", "凝固", "舞动", "飘散", "旋转", "飞舞", "荡漾", "徘徊"]
            },
            "听觉": {
                "声音": ["清脆", "沉闷", "尖锐", "低沉", "悠扬", "嘈杂", "寂静", "沙沙"],
                "音量": ["细微", "洪亮", "震耳", "轻柔", "微弱", "巨大", "低语", "咆哮"],
                "节奏": ["急促", "缓慢", "断续", "连贯", "规律", "杂乱", "平稳", "起伏"]
            },
            "触觉": {
                "温度": ["冰冷", "温热", "灼热", "凉爽", "温暖", "寒冷", "滚烫", "冰凉"],
                "质感": ["粗糙", "光滑", "柔软", "坚硬", "细腻", "颗粒感", "黏稠", "干燥"],
                "压力": ["沉重", "轻盈", "紧绷", "松弛", "压迫", "舒缓", "紧实", "松散"]
            },
            "嗅觉": {
                "气味": ["清香", "刺鼻", "芳香", "恶臭", "淡雅", "浓郁", "微弱", "强烈"],
                "类型": ["花香", "草木香", "金属味", "泥土味", "食物香", "焦味", "霉味", "清新"]
            },
            "味觉": {
                "味道": ["甘甜", "苦涩", "酸楚", "辛辣", "鲜美", "清淡", "浓郁", "回味"],
                "层次": ["单一", "丰富", "余韵", "回味无穷", "层次分明", "细腻", "粗犷"]
            }
        }

    def naturalize_text(
        self,
        text: str,
        style: str = "literary",
        context: Optional[Dict] = None
    ) -> str:
        """
        将机械化文本自然化

        Args:
            text: 原始文本
            style: 目标风格
            context: 上下文信息

        Returns:
            自然化后的文本
        """
        # 步骤1: 替换机械化表达
        naturalized = self._replace_mechanical_expressions(text)

        # 步骤2: 增加感官细节
        naturalized = self._add_sensory_details(naturalized, context)

        # 步骤3: 优化句式结构
        naturalized = self._optimize_sentence_structure(naturalized)

        # 步骤4: 如果有 LLM，进行最终优化
        if self.llm_client:
            naturalized = self._llm_optimize(naturalized, style, context)

        return naturalized

    def _replace_mechanical_expressions(self, text: str) -> str:
        """替换机械化表达"""
        result = text
        for mechanical, replacements in self.mechanical_replacements.items():
            if mechanical in result:
                replacement = random.choice(replacements)
                result = result.replace(mechanical, replacement)
        return result

    def _add_sensory_details(self, text: str, context: Optional[Dict]) -> str:
        """增加感官细节"""
        # 这里可以实现更复杂的感官细节添加逻辑
        # 简化版本：随机添加一些感官描述
        return text

    def _optimize_sentence_structure(self, text: str) -> str:
        """优化句式结构"""
        # 这里可以实现句式变化逻辑
        # 简化版本：保持原样
        return text

    def _llm_optimize(
        self,
        text: str,
        style: str,
        context: Optional[Dict]
    ) -> str:
        """使用 LLM 进行最终优化"""
        if not self.llm_client:
            return text

        prompt = f"""
        原文：{text}
        风格：{style}
        语境：{context or '无'}

        请将这段文字重写，使其：
        1. 更加自然流畅，避免机械化表达
        2. 具有画面感和感官细节
        3. 符合文学创作标准
        4. 保持原意不变

        重写后的文本：
        """

        try:
            return self.llm_client.generate(prompt)
        except:
            return text

    def describe_emotion(
        self,
        emotion: str,
        intensity: int = 3,
        character_name: Optional[str] = None
    ) -> str:
        """
        描述情感

        Args:
            emotion: 情感类型
            intensity: 强度 (1-5)
            character_name: 角色名（可选）

        Returns:
            情感描述
        """
        manifestation = EmotionNuance.get_emotion_manifestation(emotion, intensity)

        if character_name:
            return f"{character_name}{manifestation}"
        else:
            return manifestation

    def describe_mixed_emotions(
        self,
        emotions: List[Tuple[str, float]],
        character_name: Optional[str] = None
    ) -> str:
        """
        描述混合情感

        Args:
            emotions: 情感列表，每个元素为 (情感类型, 权重)
            character_name: 角色名（可选）

        Returns:
            混合情感描述
        """
        blended = self.emotion_blender.blend_emotions(emotions)

        if character_name:
            return f"{character_name}{blended['description']}"
        else:
            return blended['description']

    def enhance_description(
        self,
        subject: str,
        description: str,
        sensory_modality: Optional[str] = None
    ) -> str:
        """
        增强描述

        Args:
            subject: 描述对象
            description: 基础描述
            sensory_modality: 感官模态（视觉、听觉、触觉等）

        Returns:
            增强后的描述
        """
        # 这里可以实现更复杂的描述增强逻辑
        enhanced = description

        # 如果指定了感官模态，添加相应的感官词汇
        if sensory_modality and sensory_modality in self.sensory_vocabulary:
            vocab = self.sensory_vocabulary[sensory_modality]
            # 简化：随机选择一个词汇添加
            category = random.choice(list(vocab.keys()))
            word = random.choice(vocab[category])
            enhanced = f"{enhanced}，呈现出{word}的特质"

        return enhanced


# 便捷函数
def naturalize(text: str, style: str = "literary") -> str:
    """快速自然化文本"""
    enhancer = NaturalLanguageEnhancer()
    return enhancer.naturalize_text(text, style)


def describe_emotion_naturally(emotion: str, intensity: int = 3) -> str:
    """快速描述情感"""
    enhancer = NaturalLanguageEnhancer()
    return enhancer.describe_emotion(emotion, intensity)
