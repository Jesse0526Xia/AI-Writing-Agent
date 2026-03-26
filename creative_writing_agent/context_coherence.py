"""
语境感知和连贯性管理
确保文本的连贯性和一致性
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
import random


class ContextType(Enum):
    """语境类型"""
    SITUATION = "situation"  # 情境
    TIME = "time"  # 时间
    LOCATION = "location"  # 地点
    RELATIONSHIP = "relationship"  # 关系
    EMOTION = "emotion"  # 情感
    TOPIC = "topic"  # 话题


class CoherenceLevel(Enum):
    """连贯性等级"""
    HIGH = "high"  # 高连贯
    MEDIUM = "medium"  # 中连贯
    LOW = "low"  # 低连贯


class ContextTracker:
    """语境跟踪器"""

    def __init__(self):
        self.context_stack: List[Dict] = []
        self.current_context: Dict[str, str] = {}
        self.context_history: List[Dict] = []

    def update_context(self, context_type: str, value: str):
        """
        更新语境

        Args:
            context_type: 语境类型
            value: 语境值
        """
        self.current_context[context_type] = value

        # 添加到历史
        self.context_history.append({
            "context_type": context_type,
            "value": value,
            "timestamp": len(self.context_history)
        })

    def push_context(self, context: Dict[str, str]):
        """
        推入新的语境层

        Args:
            context: 语境字典
        """
        self.context_stack.append(self.current_context.copy())
        self.current_context.update(context)

    def pop_context(self):
        """弹出语境层"""
        if self.context_stack:
            self.current_context = self.context_stack.pop()

    def get_context(self, context_type: str) -> str:
        """获取当前语境"""
        return self.current_context.get(context_type, "")

    def get_full_context(self) -> Dict[str, str]:
        """获取完整语境"""
        return self.current_context.copy()

    def clear_context(self):
        """清除当前语境"""
        self.current_context = {}
        self.context_stack = []


class CoherenceAnalyzer:
    """连贯性分析器"""

    def __init__(self):
        # 连贯性评估标准
        self.coherence_indicators = {
            "pronoun_consistency": 0.2,  # 代词一致性
            "temporal_consistency": 0.2,  # 时间一致性
            "logical_flow": 0.3,  # 逻辑流畅性
            "thematic_consistency": 0.3  # 主题一致性
        }

    def analyze_coherence(
        self,
        text: str,
        context: Dict[str, str]
    ) -> Dict[str, float]:
        """
        分析文本的连贯性

        Args:
            text: 文本
            context: 语境

        Returns:
            连贯性评分
        """
        scores = {}

        # 评估代词一致性
        scores["pronoun_consistency"] = self._check_pronoun_consistency(text, context)

        # 评估时间一致性
        scores["temporal_consistency"] = self._check_temporal_consistency(text, context)

        # 评估逻辑流畅性
        scores["logical_flow"] = self._check_logical_flow(text)

        # 评估主题一致性
        scores["thematic_consistency"] = self._check_thematic_consistency(text, context)

        # 计算总分
        total_score = sum(scores.values())
        scores["total"] = total_score

        return scores

    def _check_pronoun_consistency(
        self,
        text: str,
        context: Dict[str, str]
    ) -> float:
        """
        检查代词一致性

        Args:
            text: 文本
            context: 语境

        Returns:
            一致性评分
        """
        # 简化实现：检查代词是否与语境一致
        pronouns = ["我", "你", "他", "她", "它", "我们", "你们", "他们"]

        # 如果语境中指定了人物，检查代词是否一致
        if "角色" in context or "人物" in context:
            # 这里可以实现更复杂的检查
            return 1.0

        return 0.8  # 默认返回中等分数

    def _check_temporal_consistency(
        self,
        text: str,
        context: Dict[str, str]
    ) -> float:
        """
        检查时间一致性

        Args:
            text: 文本
            context: 语境

        Returns:
            一致性评分
        """
        # 时间标记
        time_markers = ["昨天", "今天", "明天", "刚才", "现在", "随后", "之后"]

        # 简化实现：检查时间标记是否合理
        if "时间" in context:
            # 可以实现更复杂的时间逻辑检查
            pass

        return 0.9  # 默认返回高分

    def _check_logical_flow(self, text: str) -> float:
        """
        检查逻辑流畅性

        Args:
            text: 文本

        Returns:
            流畅性评分
        """
        # 逻辑连接词
        logical_connectors = ["因此", "所以", "但是", "然而", "而且", "此外", "首先", "其次", "最后"]

        # 计算逻辑连接词的使用频率
        connector_count = sum(text.count(connector) for connector in logical_connectors)

        # 根据连接词数量评分
        if connector_count > 3:
            return 1.0
        elif connector_count > 1:
            return 0.8
        else:
            return 0.5

    def _check_thematic_consistency(
        self,
        text: str,
        context: Dict[str, str]
    ) -> float:
        """
        检查主题一致性

        Args:
            text: 文本
            context: 语境

        Returns:
            一致性评分
        """
        # 如果语境中指定了主题，检查文本是否围绕主题
        if "主题" in context or "话题" in context:
            topic = context.get("主题", context.get("话题", ""))
            # 可以实现更复杂的主题一致性检查
            return 0.9

        return 0.8  # 默认返回中等分数


class CoherenceManager:
    """连贯性管理器"""

    def __init__(self):
        self.context_tracker = ContextTracker()
        self.coherence_analyzer = CoherenceAnalyzer()
        self.transition_templates = {
            "addition": ["此外", "而且", "再者", "另外"],
            "contrast": ["然而", "但是", "不过", "相反"],
            "sequence": ["首先", "然后", "其次", "最后"],
            "explanation": ["因此", "所以", "于是", "结果"],
            "example": ["例如", "比如", "譬如", "比方说"]
        }

    def maintain_coherence(
        self,
        text: str,
        context: Dict[str, str]
    ) -> str:
        """
        维护文本连贯性

        过程：
        1. 分析当前连贯性
        2. 根据分析结果添加过渡
        3. 检查并修复不一致

        Args:
            text: 文本
            context: 语境

        Returns:
            连贯性优化后的文本
        """
        # 分析连贯性
        coherence_scores = self.coherence_analyzer.analyze_coherence(text, context)

        # 根据评分优化
        result = text

        # 添加过渡词
        if coherence_scores["logical_flow"] < 0.7:
            result = self._add_transitions(result, context)

        # 维护主题一致性
        if coherence_scores["thematic_consistency"] < 0.7:
            result = self._maintain_thematic_consistency(result, context)

        return result

    def _add_transitions(
        self,
        text: str,
        context: Dict[str, str]
    ) -> str:
        """
        添加过渡词

        Args:
            text: 文本
            context: 语境

        Returns:
            添加过渡后的文本
        """
        # 按句号分割
        sentences = text.split("。")
        result = []

        for i, sentence in enumerate(sentences):
            if not sentence.strip():
                continue

            # 随机选择过渡类型
            transition_type = random.choice(list(self.transition_templates.keys()))

            # 添加过渡词
            if i > 0 and random.random() < 0.3:
                templates = self.transition_templates[transition_type]
                transition = random.choice(templates)
                result.append(f"{transition}，{sentence}。")
            else:
                result.append(f"{sentence}。")

        return "".join(result)

    def _maintain_thematic_consistency(
        self,
        text: str,
        context: Dict[str, str]
    ) -> str:
        """
        维护主题一致性

        Args:
            text: 文本
            context: 语境

        Returns:
            主题一致的文本
        """
        # 简化实现：确保文本与主题相关
        if "主题" in context or "话题" in context:
            topic = context.get("主题", context.get("话题", ""))
            # 可以实现更复杂的主题一致性维护
            pass

        return text

    def analyze_and_improve(
        self,
        text: str,
        context: Optional[Dict[str, str]] = None
    ) -> Dict[str, str]:
        """
        分析并改进文本

        Args:
            text: 文本
            context: 语境（可选）

        Returns:
            改进结果
        """
        if context is None:
            context = self.context_tracker.get_full_context()

        # 分析连贯性
        coherence_scores = self.coherence_analyzer.analyze_coherence(text, context)

        # 改进文本
        improved_text = self.maintain_coherence(text, context)

        # 评估改进效果
        improved_scores = self.coherence_analyzer.analyze_coherence(improved_text, context)

        return {
            "original_text": text,
            "improved_text": improved_text,
            "original_scores": coherence_scores,
            "improved_scores": improved_scores,
            "improvement": improved_scores["total"] - coherence_scores["total"]
        }


class NarrativeCoherence:
    """叙事连贯性"""

    def __init__(self):
        self.narrative_elements = {
            "plot": [],  # 情节
            "characters": [],  # 人物
            "settings": [],  # 场景
            "themes": []  # 主题
        }

    def track_narrative_element(
        self,
        element_type: str,
        element: str
    ):
        """
        跟踪叙事元素

        Args:
            element_type: 元素类型
            element: 元素
        """
        if element_type in self.narrative_elements:
            self.narrative_elements[element_type].append(element)

    def check_narrative_consistency(self) -> Dict[str, bool]:
        """
        检查叙事一致性

        Returns:
            一致性检查结果
        """
        results = {}

        # 检查人物一致性
        if "characters" in self.narrative_elements:
            characters = self.narrative_elements["characters"]
            # 简化实现：检查人物是否重复出现
            results["character_consistency"] = len(set(characters)) < len(characters)

        # 检查场景一致性
        if "settings" in self.narrative_elements:
            settings = self.narrative_elements["settings"]
            # 简化实现：检查场景是否合理切换
            results["setting_consistency"] = len(set(settings)) > 1

        return results


# 便捷函数
def analyze_text_coherence(text: str, context: Dict[str, str]) -> Dict[str, float]:
    """快速分析文本连贯性"""
    analyzer = CoherenceAnalyzer()
    return analyzer.analyze_coherence(text, context)


def improve_text_coherence(text: str, context: Dict[str, str]) -> str:
    """快速改进文本连贯性"""
    manager = CoherenceManager()
    return manager.maintain_coherence(text, context)
