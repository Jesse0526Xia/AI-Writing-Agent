"""
文学修辞和表达技巧模块
消除机械化表达，增加文学性和艺术性
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
import random


class MetaphorType(Enum):
    """比喻类型"""
    SIMILE = "simile"  # 明喻（使用"像"、"如"）
    METAPHOR = "metaphor"  # 暗喻（直接等同）
    METONYMY = "metonymy"  # 借喻
    PERSONIFICATION = "personification"  # 拟人
    REIFICATION = "reification"  - 拟物
    SYMBOLISM = "symbolism"  # 象征


class RhetoricalDevice(Enum):
    """修辞手法"""
    PARALLELISM = "parallelism"  # 排比
    ANTITHESIS = "antithesis"  - 对比
    REPETITION = "repetition"  # 重复
    HYPERBOLE = "hyperbole"  # 夸张
    UNDERSTATEMENT = "understatement"  # 低调陈述
    RHETORICAL_QUESTION = "rhetorical_question"  # 反问
    IRONY = "irony"  # 反讽
    ALLUSION = "allusion"  # 典故


class MetaphorGenerator:
    """比喻生成器"""

    def __init__(self):
        self.metaphor_templates = {
            MetaphorType.SIMILE: [
                "{subject}像{vehicle}一样{attribute}",
                "{subject}宛如{vehicle}",
                "{subject}仿佛{vehicle}一般",
                "{subject}好似{vehicle}"
            ],
            MetaphorType.METAPHOR: [
                "{subject}是{vehicle}",
                "{subject}成了{vehicle}",
                "{subject}化作{vehicle}",
                "{subject}便是{vehicle}"
            ],
            MetaphorType.PERSONIFICATION: [
                "{subject}{action}，仿佛{personification}",
                "{subject}也{person_action}起来",
                "{subject}带着{human_emotion}{action}",
                "{subject}像{human}一样{action}"
            ]
        }

        # 比喻素材库
        self.vehicles = {
            "自然": ["春风", "秋雨", "烈日", "寒霜", "明月", "繁星", "彩虹", "云霞"],
            "动物": ["猛虎", "雄鹰", "蝴蝶", "蚂蚁", "蜗牛", "雄狮", "飞鸟", "游鱼"],
            "物品": ["利剑", "坚盾", "明镜", "清流", "磐石", "薄冰", "丝线", "珍珠"],
            "抽象": ["梦境", "记忆", "希望", "恐惧", "时间", "命运", "真理", "谎言"]
        }

        self.attributes = {
            "柔美": ["温柔", "柔软", "柔弱", "柔顺"],
            "刚强": ["坚强", "刚毅", "坚硬", "刚猛"],
            "明亮": ["明亮", "光亮", "辉煌", "灿烂"],
            "阴暗": ["阴暗", "昏暗", "阴暗", "黯淡"],
            "快速": ["快速", "迅速", "敏捷", "飞快"],
            "缓慢": ["缓慢", "迟缓", "徐缓", "悠闲"]
        }

    def generate_metaphor(
        self,
        subject: str,
        metaphor_type: MetaphorType,
        context: Optional[str] = None
    ) -> str:
        """
        生成比喻

        Args:
            subject: 本体
            metaphor_type: 比喻类型
            context: 语境（可选）

        Returns:
            比喻句
        """
        if metaphor_type not in self.metaphor_templates:
            metaphor_type = MetaphorType.SIMILE

        templates = self.metaphor_templates[metaphor_type]
        template = random.choice(templates)

        # 选择喻体
        vehicle_category = random.choice(list(self.vehicles.keys()))
        vehicle = random.choice(self.vehicles[vehicle_category])

        # 选择属性
        attribute = None
        if "{attribute}" in template:
            attribute_category = random.choice(list(self.attributes.keys()))
            attribute = random.choice(self.attributes[attribute_category])

        # 填充模板
        if attribute:
            metaphor = template.format(
                subject=subject,
                vehicle=vehicle,
                attribute=attribute
            )
        else:
            metaphor = template.format(
                subject=subject,
                vehicle=vehicle
            )

        return metaphor

    def generate_personification(
        self,
        subject: str,
        action: str,
        human_emotion: Optional[str] = None
    ) -> str:
        """
        生成拟人句

        Args:
            subject: 主体
            action: 动作
            human_emotion: 人类情感（可选）

        Returns:
            拟人句
        """
        personifications = [
            f"{subject}{action}，仿佛有了生命",
            f"{subject}带着{human_emotion or '喜悦'}{action}",
            f"{subject}像个孩子一样{action}",
            f"{subject}也{action}起来，充满了灵性"
        ]

        return random.choice(personifications)


class RhetoricalDeviceGenerator:
    """修辞手法生成器"""

    def __init__(self):
        self.device_templates = {
            RhetoricalDevice.PARALLELISM: {
                "template": "{item1}，{item2}，{item3}",
                "description": "排比句"
            },
            RhetoricalDevice.ANTITHESIS: {
                "template": "{positive}，{negative}",
                "description": "对比句"
            },
            RhetoricalDevice.REPETITION: {
                "template": "{phrase}，{phrase}，{phrase}",
                "description": "重复句"
            },
            RhetoricalDevice.HYPERBOLE: {
                "template": "{subject}{exaggerated_action}",
                "description": "夸张句"
            },
            RhetoricalDevice.RHETORICAL_QUESTION: {
                "template": "难道{question}吗？",
                "description": "反问句"
            }
        }

    def generate_parallelism(
        self,
        items: List[str],
        structure: str = "simple"
    ) -> str:
        """
        生成排比句

        Args:
            items: 排比项目
            structure: 结构类型

        Returns:
            排比句
        """
        if len(items) < 2:
            return "，".join(items)

        if structure == "simple":
            return "，".join(items)
        elif structure == "elaborate":
            return "；".join(items)
        else:
            return "，".join(items)

    def generate_antithesis(
        self,
        positive: str,
        negative: str,
        connector: str = "却"
    ) -> str:
        """
        生成对比句

        Args:
            positive: 正面描述
            negative: 负面描述
            connector: 连接词

        Returns:
            对比句
        """
        return f"{positive}{connector}{negative}"

    def generate_hyperbole(
        self,
        subject: str,
        action: str,
        intensity: str = "high"
    ) -> str:
        """
        生成夸张句

        Args:
            subject: 主体
            action: 动作
            intensity: 强度

        Returns:
            夸张句
        """
        exaggerations = {
            "high": ["简直要...", "几乎要...", "恨不得...", "简直..."],
            "medium": ["非常...", "特别...", "极其...", "十分..."],
            "low": ["很...", "挺...", "相当...", "颇为..."]
        }

        exag = random.choice(exaggerations.get(intensity, exaggerations["high"]))
        return f"{subject}{exag}{action}"

    def generate_rhetorical_question(
        self,
        statement: str,
        emphasis: str = "strong"
    ) -> str:
        """
        生成反问句

        Args:
            statement: 陈述句
            emphasis: 强调程度

        Returns:
            反问句
        """
        if emphasis == "strong":
            return f"难道{statement}吗？"
        else:
            return f"难道不是{statement}吗？"


class SensoryDescriptionEnhancer:
    """感官描述增强器"""

    def __init__(self):
        self.sensory_vocabulary = {
            "视觉": {
                "颜色": ["绯红", "苍白", "黯淡", "璀璨", "湛蓝", "翠绿", "金黄", "银白",
                         "嫣红", "墨黑", "素白", "葱绿", "橘黄", "紫罗兰", "天青"],
                "光影": ["斑驳", "朦胧", "刺眼", "柔和", "昏暗", "明亮", "闪烁", "摇曳",
                         "流转", "跃动", "弥漫", "洒落", "投射", "笼罩", "穿透"],
                "动态": ["流淌", "凝固", "舞动", "飘散", "旋转", "飞舞", "荡漾", "徘徊",
                         "翻滚", "跳跃", "滑落", "升腾", "弥漫", "舒展", "卷曲"],
                "形状": ["蜿蜒", "笔直", "曲折", "圆润", "尖锐", "平坦", "崎岖", "陡峭",
                         "修长", "粗壮", "纤细", "庞大", "微小", "宽阔", "狭窄"]
            },
            "听觉": {
                "声音": ["清脆", "沉闷", "尖锐", "低沉", "悠扬", "嘈杂", "寂静", "沙沙",
                         "轰鸣", "低语", "咆哮", "呢喃", "吟唱", "哀鸣", "欢唱"],
                "音量": ["细微", "洪亮", "震耳", "轻柔", "微弱", "巨大", "低语", "咆哮",
                         "如雷贯耳", "细若游丝", "震耳欲聋", "轻如蚊呐"],
                "节奏": ["急促", "缓慢", "断续", "连贯", "规律", "杂乱", "平稳", "起伏",
                         "抑扬顿挫", "铿锵有力", "舒缓悠扬", "杂乱无章"],
                "音色": ["清亮", "浑厚", "沙哑", "柔和", "尖锐", "低沉", "高亢", "圆润",
                         "磁性", "甜美", "粗犷", "细腻", "纯净", "浑浊"]
            },
            "嗅觉": {
                "气味": ["清香", "刺鼻", "芳香", "恶臭", "淡雅", "浓郁", "微弱", "强烈",
                         "芬芳", "腥臭", "霉味", "焦味", "清香", "腥膻", "馥郁"],
                "浓度": ["淡雅", "浓郁", "微弱", "强烈", "若有若无", "扑面而来", "沁人心脾",
                         "令人窒息", "清香扑鼻", "浓烈刺鼻"],
                "类型": ["花香", "草木香", "金属味", "泥土味", "食物香", "焦味", "霉味", "清新",
                         "书香", "墨香", "茶香", "酒香", "脂粉香", "烟火气", "海腥味"]
            },
            "触觉": {
                "温度": ["冰冷", "温热", "灼热", "凉爽", "温暖", "寒冷", "滚烫", "冰凉",
                         "温暖如春", "冰冷刺骨", "炎热如火", "凉意袭人"],
                "质感": ["粗糙", "光滑", "柔软", "坚硬", "细腻", "颗粒感", "黏稠", "干燥",
                         "丝滑", "毛糙", "坚实", "松软", "黏腻", "干涩"],
                "压力": ["沉重", "轻盈", "紧绷", "松弛", "压迫", "舒缓", "紧实", "松散",
                         "沉重如山", "轻如鸿毛", "压迫感强", "轻松自如"],
                "触感": ["刺痛", "酥麻", "瘙痒", "灼烧", "冰冷", "温暖", "柔软", "坚硬",
                         "细腻如丝", "粗糙如砂", "温暖如棉", "冰冷如铁"]
            },
            "味觉": {
                "味道": ["甘甜", "苦涩", "酸楚", "辛辣", "鲜美", "清淡", "浓郁", "回味",
                         "甜腻", "苦不堪言", "酸涩难忍", "辛辣刺鼻", "鲜美可口"],
                "层次": ["单一", "丰富", "余韵", "回味无穷", "层次分明", "细腻", "粗犷",
                         "五味杂陈", "百味俱全", "回味悠长", "层次丰富"],
                "口感": ["爽脆", "绵软", "劲道", "酥脆", "软糯", "Q弹", "细腻", "粗糙",
                         "入口即化", "回味无穷", "齿颊留香", "余味悠长"]
            }
        }

    def enhance_with_sensory_details(
        self,
        description: str,
        modality: str = "visual",
        intensity: str = "medium"
    ) -> str:
        """
        用感官细节增强描述

        Args:
            description: 基础描述
            modality: 感官模态
            intensity: 强度

        Returns:
            增强后的描述
        """
        if modality not in self.sensory_vocabulary:
            modality = "视觉"

        vocab = self.sensory_vocabulary[modality]

        # 随机选择一个类别
        category = random.choice(list(vocab.keys()))
        words = vocab[category]

        # 选择一个词
        word = random.choice(words)

        # 根据强度调整
        if intensity == "high":
            # 使用更强烈的词
            enhanced = f"{description}，呈现出{word}的特质"
        elif intensity == "low":
            # 使用更温和的词
            enhanced = f"{description}，带有{word}的感觉"
        else:
            # 中等强度
            enhanced = f"{description}，显得{word}"

        return enhanced

    def combine_sensory_modalities(
        self,
        description: str,
        modalities: List[str]
    ) -> str:
        """
        组合多种感官模态

        Args:
            description: 基础描述
            modalities: 感官模态列表

        Returns:
            组合后的描述
        """
        result = description

        for modality in modalities:
            if modality in self.sensory_vocabulary:
                result = self.enhance_with_sensory_details(
                    result,
                    modality,
                    intensity="medium"
                )

        return result


class SentenceRhythmOptimizer:
    """句子韵律优化器"""

    def __init__(self):
        self.sentence_patterns = {
            "short": [],  # 短句（5-10字）
            "medium": [],  # 中句（10-20字）
            "long": [],  # 长句（20字以上）
            "complex": []  # 复合句
        }

    def vary_sentence_length(self, text: str) -> str:
        """
        变化句子长度

        Args:
            text: 原始文本

        Returns:
            变化后的文本
        """
        # 简化实现：按句号分割并随机调整
        sentences = text.split("。")
        varied = []

        for sentence in sentences:
            if not sentence.strip():
                continue

            words = sentence.split()

            # 随机决定是否扩展或简化
            if len(words) > 15 and random.random() < 0.3:
                # 简化长句
                varied.append(" ".join(words[:len(words)//2]) + "。")
            elif len(words) < 8 and random.random() < 0.3:
                # 扩展短句
                varied.append(sentence + "，" + sentence + "。")
            else:
                varied.append(sentence + "。")

        return "".join(varied)

    def add_rhythmic_patterns(self, text: str) -> str:
        """
        添加韵律模式

        Args:
            text: 原始文本

        Returns:
            添加韵律后的文本
        """
        # 简化实现：添加一些韵律标记
        return text


class LiteraryTechniquesIntegrator:
    """文学技巧整合器"""

    def __init__(self, llm_client=None):
        self.llm_client = llm_client
        self.metaphor_generator = MetaphorGenerator()
        self.rhetorical_generator = RhetoricalDeviceGenerator()
        self.sensory_enhancer = SensoryDescriptionEnhancer()
        self.rhythm_optimizer = SentenceRhythmOptimizer()

    def enhance_text(
        self,
        text: str,
        techniques: Optional[List[str]] = None,
        llm_generate_func: Optional[callable] = None
    ) -> str:
        """
        整合多种文学技巧增强文本

        Args:
            text: 原始文本
            techniques: 使用的技巧列表
            llm_generate_func: LLM 生成函数（可选）

        Returns:
            增强后的文本
        """
        if techniques is None:
            techniques = ["sensory", "metaphor", "rhythm"]

        result = text

        # 应用感官增强
        if "sensory" in techniques:
            result = self.sensory_enhancer.enhance_with_sensory_details(
                result,
                modality="视觉",
                intensity="medium"
            )

        # 应用比喻
        if "metaphor" in techniques:
            # 简化实现：不自动添加比喻，避免过度修饰
            pass

        # 优化韵律
        if "rhythm" in techniques:
            result = self.rhythm_optimizer.vary_sentence_length(result)

        # 如果有 LLM，进行最终优化
        if llm_generate_func:
            result = self._llm_optimize(result, techniques)

        return result

    def _llm_optimize(
        self,
        text: str,
        techniques: List[str]
    ) -> str:
        """使用 LLM 优化文本"""
        if not self.llm_client:
            return text

        techniques_desc = {
            "sensory": "增加感官细节",
            "metaphor": "使用比喻和意象",
            "rhythm": "优化句子韵律",
            "rhetorical": "使用修辞手法"
        }

        applied_techniques = [
            techniques_desc.get(t, t) for t in techniques if t in techniques_desc
        ]

        prompt = f"""
        原文：{text}
        应用的技巧：{', '.join(applied_techniques)}

        请将这段文字重写，使其：
        1. 更加生动形象，具有文学性
        2. 自然流畅，避免过度修饰
        3. 符合文学创作标准
        4. 保持原意不变

        优化后的文本：
        """

        try:
            return self.llm_client.generate(prompt)
        except:
            return text


# 便捷函数
def add_metaphor(subject: str, metaphor_type: str = "simile") -> str:
    """快速添加比喻"""
    generator = MetaphorGenerator()
    return generator.generate_metaphor(
        subject,
        MetaphorType(metaphor_type)
    )


def enhance_description(description: str, modality: str = "visual") -> str:
    """快速增强描述"""
    enhancer = SensoryDescriptionEnhancer()
    return enhancer.enhance_with_sensory_details(
        description,
        modality
    )


def apply_literary_techniques(text: str) -> str:
    """快速应用文学技巧"""
    integrator = LiteraryTechniquesIntegrator()
    return integrator.enhance_text(text)
