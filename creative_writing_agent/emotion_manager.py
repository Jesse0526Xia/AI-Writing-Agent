"""
情感弧线管理系统
负责情感节点规划、情感曲线管理、情感转换等
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
import json
from dataclasses import dataclass


class EmotionIntensity(Enum):
    """情感强度"""
    VERY_LOW = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    VERY_HIGH = 5


class EmotionCategory(Enum):
    """情感类别"""
    POSITIVE = "positive"  # 积极情感
    NEGATIVE = "negative"  # 消极情感
    NEUTRAL = "neutral"  # 中性情感
    MIXED = "mixed"  # 混合情感


@dataclass
class EmotionNode:
    """情感节点"""
    node_id: str
    emotion_type: str  # 具体情感类型（如：快乐、悲伤、愤怒等）
    category: EmotionCategory
    intensity: EmotionIntensity
    description: str
    plot_point_id: Optional[str] = None  # 关联的情节点ID
    character_name: Optional[str] = None  # 关联的角色名
    position: float = 0.0  # 在故事中的位置 (0.0 - 1.0)
    duration: float = 0.1  # 持续时间比例


class EmotionManager:
    """情感弧线管理器"""

    def __init__(self, llm_client=None):
        """
        初始化情感管理器

        Args:
            llm_client: LLM 客户端
        """
        self.llm_client = llm_client
        self.emotion_nodes: Dict[str, EmotionNode] = {}
        self.emotion_arcs: Dict[str, List[EmotionNode]] = {}  # 角色名 -> 情感节点列表
        self.emotion_templates = self._load_emotion_templates()

    def _load_emotion_templates(self) -> Dict[str, Dict]:
        """加载情感模板"""
        return {
            "快乐": {
                "category": EmotionCategory.POSITIVE,
                "default_intensity": EmotionIntensity.MEDIUM,
                "triggers": ["成功", "获得", "惊喜", "团聚"],
                "expressions": ["微笑", "大笑", "欢呼", "跳跃"]
            },
            "悲伤": {
                "category": EmotionCategory.NEGATIVE,
                "default_intensity": EmotionIntensity.MEDIUM,
                "triggers": ["失去", "失败", "离别", "失望"],
                "expressions": ["流泪", "沉默", "叹息", "低头"]
            },
            "愤怒": {
                "category": EmotionCategory.NEGATIVE,
                "default_intensity": EmotionIntensity.HIGH,
                "triggers": ["背叛", "不公", "羞辱", "威胁"],
                "expressions": ["皱眉", "握拳", "大喊", "摔东西"]
            },
            "恐惧": {
                "category": EmotionCategory.NEGATIVE,
                "default_intensity": EmotionIntensity.HIGH,
                "triggers": ["危险", "未知", "威胁", "黑暗"],
                "expressions": ["颤抖", "后退", "屏住呼吸", "瞪大眼睛"]
            },
            "惊讶": {
                "category": EmotionCategory.NEUTRAL,
                "default_intensity": EmotionIntensity.MEDIUM,
                "triggers": ["意外", "揭示", "突发", "反常"],
                "expressions": ["张嘴", "瞪眼", "倒吸一口气", "愣住"]
            },
            "希望": {
                "category": EmotionCategory.POSITIVE,
                "default_intensity": EmotionIntensity.MEDIUM,
                "triggers": ["机会", "转机", "支持", "灵感"],
                "expressions": ["眼神明亮", "挺胸", "微笑", "点头"]
            },
            "绝望": {
                "category": EmotionCategory.NEGATIVE,
                "default_intensity": EmotionIntensity.VERY_HIGH,
                "triggers": ["失败", "孤立", "无路可退", "失去一切"],
                "expressions": ["垂头", "流泪", "沉默", "放弃"]
            },
            "爱": {
                "category": EmotionCategory.POSITIVE,
                "default_intensity": EmotionIntensity.HIGH,
                "triggers": ["相遇", "理解", "关怀", "牺牲"],
                "expressions": ["温柔", "拥抱", "凝视", "微笑"]
            },
            "恨": {
                "category": EmotionCategory.NEGATIVE,
                "default_intensity": EmotionIntensity.VERY_HIGH,
                "triggers": ["伤害", "背叛", "嫉妒", "仇恨"],
                "expressions": ["怒视", "冷笑", "咬牙", "躲避"]
            },
            "平静": {
                "category": EmotionCategory.NEUTRAL,
                "default_intensity": EmotionIntensity.LOW,
                "triggers": ["日常", "安全", "稳定", "习惯"],
                "expressions": ["放松", "呼吸平稳", "正常", "自然"]
            }
        }

    def create_emotion_node(
        self,
        node_id: str,
        emotion_type: str,
        intensity: int,
        description: str,
        position: float = 0.0,
        **kwargs
    ) -> EmotionNode:
        """
        创建情感节点

        Args:
            node_id: 节点ID
            emotion_type: 情感类型
            intensity: 强度 (1-5)
            description: 描述
            position: 位置 (0.0 - 1.0)
            **kwargs: 其他属性

        Returns:
            情感节点
        """
        # 获取情感模板
        template = self.emotion_templates.get(emotion_type, {
            "category": EmotionCategory.NEUTRAL,
            "default_intensity": EmotionIntensity.MEDIUM
        })

        emotion_node = EmotionNode(
            node_id=node_id,
            emotion_type=emotion_type,
            category=template["category"],
            intensity=EmotionIntensity(intensity),
            description=description,
            plot_point_id=kwargs.get("plot_point_id"),
            character_name=kwargs.get("character_name"),
            position=position,
            duration=kwargs.get("duration", 0.1)
        )

        self.emotion_nodes[node_id] = emotion_node

        # 添加到角色的情感弧线
        if kwargs.get("character_name"):
            char_name = kwargs["character_name"]
            if char_name not in self.emotion_arcs:
                self.emotion_arcs[char_name] = []
            self.emotion_arcs[char_name].append(emotion_node)

        return emotion_node

    def plan_emotional_arc(
        self,
        character_name: str,
        story_length: float = 1.0,
        arc_type: str = "classic"
    ) -> List[EmotionNode]:
        """
        规划情感弧线

        Args:
            character_name: 角色名
            story_length: 故事长度比例
            arc_type: 弧线类型（classic: 经典, tragedy: 悲剧, comedy: 喜剧, redemptive: 救赎）

        Returns:
            情感节点列表
        """
        arc_patterns = {
            "classic": [
                (0.1, "平静", 2, "故事开始时的平静状态"),
                (0.2, "惊讶", 3, "激励事件带来的惊讶"),
                (0.3, "希望", 3, "开始行动时的希望"),
                (0.5, "恐惧", 4, "面临挑战的恐惧"),
                (0.7, "绝望", 5, "最低点的绝望"),
                (0.85, "愤怒", 4, "反击的愤怒"),
                (0.95, "快乐", 4, "成功后的喜悦"),
                (1.0, "平静", 2, "结局的平静")
            ],
            "tragedy": [
                (0.1, "平静", 2, "平静的开始"),
                (0.2, "希望", 3, "充满希望"),
                (0.4, "快乐", 4, "达到巅峰"),
                (0.6, "恐惧", 3, "危机出现"),
                (0.8, "绝望", 5, "彻底失败"),
                (1.0, "悲伤", 5, "悲剧结局")
            ],
            "comedy": [
                (0.1, "平静", 2, "正常状态"),
                (0.2, "惊讶", 3, "意外的麻烦"),
                (0.4, "恐惧", 3, "混乱加剧"),
                (0.6, "快乐", 4, "转机出现"),
                (0.8, "惊讶", 3, "最后的转折"),
                (1.0, "快乐", 5, "大团圆结局")
            ],
            "redemptive": [
                (0.1, "悲伤", 3, "过去的创伤"),
                (0.2, "愤怒", 4, "对现状的不满"),
                (0.3, "恐惧", 3, "面对改变的恐惧"),
                (0.5, "希望", 3, "看到转机"),
                (0.7, "绝望", 4, "再次受挫"),
                (0.9, "爱", 5, "获得救赎"),
                (1.0, "平静", 3, "内心的平静")
            ]
        }

        pattern = arc_patterns.get(arc_type, arc_patterns["classic"])
        emotion_nodes = []

        for i, (position, emotion_type, intensity, description) in enumerate(pattern):
            node_id = f"{character_name}_emotion_{i+1}"
            emotion_node = self.create_emotion_node(
                node_id=node_id,
                emotion_type=emotion_type,
                intensity=intensity,
                description=description,
                position=position,
                character_name=character_name
            )
            emotion_nodes.append(emotion_node)

        return emotion_nodes

    def get_emotion_at_position(
        self,
        character_name: str,
        position: float
    ) -> Optional[EmotionNode]:
        """
        获取指定位置的情感

        Args:
            character_name: 角色名
            position: 位置 (0.0 - 1.0)

        Returns:
            情感节点
        """
        if character_name not in self.emotion_arcs:
            return None

        emotion_arc = self.emotion_arcs[character_name]

        # 找到最接近位置的情感节点
        closest_node = None
        min_distance = float('inf')

        for node in emotion_arc:
            distance = abs(node.position - position)
            if distance < min_distance:
                min_distance = distance
                closest_node = node

        return closest_node

    def get_emotion_transition(
        self,
        character_name: str,
        from_position: float,
        to_position: float
    ) -> Tuple[Optional[EmotionNode], Optional[EmotionNode]]:
        """
        获取情感转换

        Args:
            character_name: 角色名
            from_position: 起始位置
            to_position: 结束位置

        Returns:
            (起始情感, 结束情感)
        """
        from_emotion = self.get_emotion_at_position(character_name, from_position)
        to_emotion = self.get_emotion_at_position(character_name, to_position)

        return from_emotion, to_emotion

    def smooth_emotional_curve(
        self,
        character_name: str,
        smoothing_factor: float = 0.3
    ) -> List[EmotionNode]:
        """
        平滑情感曲线

        Args:
            character_name: 角色名
            smoothing_factor: 平滑因子 (0.0 - 1.0)

        Returns:
            平滑后的情感节点列表
        """
        if character_name not in self.emotion_arcs:
            return []

        emotion_arc = sorted(
            self.emotion_arcs[character_name],
            key=lambda x: x.position
        )

        if len(emotion_arc) < 3:
            return emotion_arc

        # 应用简单的移动平均平滑
        smoothed_arc = []
        for i, node in enumerate(emotion_arc):
            if i == 0 or i == len(emotion_arc) - 1:
                smoothed_arc.append(node)
            else:
                # 计算平滑后的强度
                prev_intensity = emotion_arc[i-1].intensity.value
                curr_intensity = node.intensity.value
                next_intensity = emotion_arc[i+1].intensity.value

                smoothed_intensity = (
                    prev_intensity * smoothing_factor +
                    curr_intensity * (1 - 2 * smoothing_factor) +
                    next_intensity * smoothing_factor
                )

                # 创建新的情感节点
                smoothed_node = EmotionNode(
                    node_id=f"{node.node_id}_smoothed",
                    emotion_type=node.emotion_type,
                    category=node.category,
                    intensity=EmotionIntensity(max(1, min(5, round(smoothed_intensity)))),
                    description=node.description,
                    plot_point_id=node.plot_point_id,
                    character_name=node.character_name,
                    position=node.position,
                    duration=node.duration
                )
                smoothed_arc.append(smoothed_node)

        return smoothed_arc

    def generate_emotion_description(
        self,
        emotion_type: str,
        intensity: int,
        character_name: Optional[str] = None
    ) -> str:
        """
        生成情感描述

        Args:
            emotion_type: 情感类型
            intensity: 强度 (1-5)
            character_name: 角色名（可选）

        Returns:
            情感描述
        """
        template = self.emotion_templates.get(emotion_type, {})

        intensity_desc = {
            1: "轻微的",
            2: "淡淡的",
            3: "明显的",
            4: "强烈的",
            5: "极度的"
        }

        base_desc = f"{intensity_desc.get(intensity, '')}{emotion_type}"

        if character_name:
            return f"{character_name}感到{base_desc}"
        else:
            return base_desc

    def analyze_emotional_arc(self, character_name: str) -> Dict:
        """
        分析情感弧线

        Args:
            character_name: 角色名

        Returns:
            分析结果
        """
        if character_name not in self.emotion_arcs:
            return {
                "character": character_name,
                "status": "no_emotions",
                "message": "该角色没有情感数据"
            }

        emotion_arc = self.emotion_arcs[character_name]

        # 统计情感类别
        category_counts = {
            EmotionCategory.POSITIVE: 0,
            EmotionCategory.NEGATIVE: 0,
            EmotionCategory.NEUTRAL: 0,
            EmotionCategory.MIXED: 0
        }

        # 统计情感类型
        emotion_type_counts = {}

        # 计算平均强度
        total_intensity = 0

        for node in emotion_arc:
            category_counts[node.category] += 1
            emotion_type_counts[node.emotion_type] = emotion_type_counts.get(node.emotion_type, 0) + 1
            total_intensity += node.intensity.value

        # 确定主导情感
        dominant_category = max(category_counts, key=category_counts.get)
        dominant_emotion = max(emotion_type_counts, key=emotion_type_counts.get)

        # 计算情感波动
        if len(emotion_arc) > 1:
            intensity_values = [node.intensity.value for node in emotion_arc]
            avg_intensity = sum(intensity_values) / len(intensity_values)
            intensity_variance = sum((x - avg_intensity) ** 2 for x in intensity_values) / len(intensity_values)
            volatility = intensity_variance ** 0.5
        else:
            avg_intensity = total_intensity / len(emotion_arc) if emotion_arc else 0
            volatility = 0

        analysis = {
            "character": character_name,
            "total_emotions": len(emotion_arc),
            "category_distribution": {cat.value: count for cat, count in category_counts.items()},
            "emotion_type_distribution": emotion_type_counts,
            "dominant_category": dominant_category.value,
            "dominant_emotion": dominant_emotion,
            "average_intensity": round(avg_intensity, 2),
            "volatility": round(volatility, 2),
            "arc_shape": self._determine_arc_shape(emotion_arc)
        }

        return analysis

    def _determine_arc_shape(self, emotion_arc: List[EmotionNode]) -> str:
        """确定情感弧线形状"""
        if len(emotion_arc) < 3:
            return "insufficient_data"

        # 简单的形状判断
        first_half = emotion_arc[:len(emotion_arc)//2]
        second_half = emotion_arc[len(emotion_arc)//2:]

        avg_first = sum(node.intensity.value for node in first_half) / len(first_half)
        avg_second = sum(node.intensity.value for node in second_half) / len(second_half)

        if avg_second > avg_first * 1.2:
            return "rising"  # 上升
        elif avg_second < avg_first * 0.8:
            return "falling"  # 下降
        elif avg_first > 3 and avg_second > 3:
            return "high"  # 高位
        elif avg_first < 3 and avg_second < 3:
            return "low"  # 低位
        else:
            return "mixed"  # 混合

    def export_emotions(self, filepath: str):
        """
        导出情感数据

        Args:
            filepath: 文件路径
        """
        data = {
            "emotion_nodes": {
                node_id: {
                    "emotion_type": node.emotion_type,
                    "category": node.category.value,
                    "intensity": node.intensity.value,
                    "description": node.description,
                    "plot_point_id": node.plot_point_id,
                    "character_name": node.character_name,
                    "position": node.position,
                    "duration": node.duration
                }
                for node_id, node in self.emotion_nodes.items()
            },
            "emotion_arcs": {
                char_name: [node.node_id for node in nodes]
                for char_name, nodes in self.emotion_arcs.items()
            }
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_emotions(self, filepath: str):
        """
        加载情感数据

        Args:
            filepath: 文件路径
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.emotion_nodes.clear()
        self.emotion_arcs.clear()

        # 加载情感节点
        for node_id, node_data in data["emotion_nodes"].items():
            emotion_node = EmotionNode(
                node_id=node_id,
                emotion_type=node_data["emotion_type"],
                category=EmotionCategory(node_data["category"]),
                intensity=EmotionIntensity(node_data["intensity"]),
                description=node_data["description"],
                plot_point_id=node_data.get("plot_point_id"),
                character_name=node_data.get("character_name"),
                position=node_data.get("position", 0.0),
                duration=node_data.get("duration", 0.1)
            )
            self.emotion_nodes[node_id] = emotion_node

        # 加载情感弧线
        for char_name, node_ids in data["emotion_arcs"].items():
            self.emotion_arcs[char_name] = [
                self.emotion_nodes[node_id]
                for node_id in node_ids
                if node_id in self.emotion_nodes
            ]


# 便捷函数
def create_emotion_arc(
    character_name: str,
    arc_type: str = "classic"
) -> List[EmotionNode]:
    """
    快速创建情感弧线

    Args:
        character_name: 角色名
        arc_type: 弧线类型

    Returns:
        情感节点列表
    """
    manager = EmotionManager()
    return manager.plan_emotional_arc(character_name, arc_type=arc_type)
