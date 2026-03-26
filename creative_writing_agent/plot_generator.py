"""
情节设计与发展系统
负责情节节点生成、冲突设计、转折点、情节推进等
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
import json
from datetime import datetime


class PlotType(Enum):
    """情节类型"""
    EXPOSITION = "exposition"  # 铺垫
    INCITING_INCIDENT = "inciting_incident"  # 激励事件
    RISING_ACTION = "rising_action"  # 上升动作
    CONFLICT = "conflict"  # 冲突
    CLIMAX = "climax"  # 高潮
    FALLING_ACTION = "falling_action"  - 下降动作
    RESOLUTION = "resolution"  # 结局
    TWIST = "twist"  # 转折


class ConflictType(Enum):
    """冲突类型"""
    MAN_VS_MAN = "man_vs_man"  # 人与人
    MAN_VS_SELF = "man_vs_self"  # 人与自己
    MAN_VS_NATURE = "man_vs_nature"  # 人与自然
    MAN_VS_SOCIETY = "man_vs_society"  # 人与社会
    MAN_VS_FATE = "man_vs_fate"  # 人与命运
    MAN_VS_TECHNOLOGY = "man_vs_technology"  # 人与技术


class PlotPoint:
    """情节节点"""

    def __init__(
        self,
        plot_id: str,
        plot_type: PlotType,
        description: str,
        act_number: int,
        chapter_number: Optional[int] = None,
        characters_involved: Optional[List[str]] = None,
        location: Optional[str] = None,
        stakes: str = "",
        outcome: Optional[str] = None,
        foreshadowing: Optional[List[str]] = None
    ):
        """
        初始化情节节点

        Args:
            plot_id: 情节ID
            plot_type: 情节类型
            description: 描述
            act_number: 所在幕数
            chapter_number: 所在章节数（可选）
            characters_involved: 涉及的角色
            location: 地点
            stakes: 赌注/利害关系
            outcome: 结果（可选，在生成后填充）
            foreshadowing: 伏笔列表
        """
        self.plot_id = plot_id
        self.plot_type = plot_type
        self.description = description
        self.act_number = act_number
        self.chapter_number = chapter_number
        self.characters_involved = characters_involved or []
        self.location = location or ""
        self.stakes = stakes
        self.outcome = outcome
        self.foreshadowing = foreshadowing or []
        self.completed = False
        self.dependencies = []  # 依赖的其他情节节点
        self.generated_content = ""  # 生成的内容

    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "plot_id": self.plot_id,
            "plot_type": self.plot_type.value,
            "description": self.description,
            "act_number": self.act_number,
            "chapter_number": self.chapter_number,
            "characters_involved": self.characters_involved,
            "location": self.location,
            "stakes": self.stakes,
            "outcome": self.outcome,
            "foreshadowing": self.foreshadowing,
            "completed": self.completed,
            "dependencies": self.dependencies,
            "generated_content": self.generated_content
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'PlotPoint':
        """从字典创建情节节点"""
        return cls(
            plot_id=data["plot_id"],
            plot_type=PlotType(data["plot_type"]),
            description=data["description"],
            act_number=data["act_number"],
            chapter_number=data.get("chapter_number"),
            characters_involved=data.get("characters_involved"),
            location=data.get("location"),
            stakes=data.get("stakes"),
            outcome=data.get("outcome"),
            foreshadowing=data.get("foreshadowing")
        )


class PlotGenerator:
    """情节生成器"""

    def __init__(self, llm_client=None):
        """
        初始化情节生成器

        Args:
            llm_client: LLM 客户端
        """
        self.llm_client = llm_client
        self.plot_points: Dict[str, PlotPoint] = {}
        self.plot_templates = self._load_plot_templates()
        self.conflict_templates = self._load_conflict_templates()

    def _load_plot_templates(self) -> Dict[PlotType, List[Dict]]:
        """加载情节模板"""
        return {
            PlotType.INCITING_INCIDENT: [
                {"template": "{character}发现了{object}", "elements": ["character", "object"]},
                {"template": "{character}收到了{message}", "elements": ["character", "message"]},
                {"template": "{event}突然发生在{location}", "elements": ["event", "location"]}
            ],
            PlotType.CONFLICT: [
                {"template": "{character1}与{character2}因{reason}发生争执", "elements": ["character1", "character2", "reason"]},
                {"template": "{character}面临{challenge}的考验", "elements": ["character", "challenge"]},
                {"template": "{character}必须在{choice1}和{choice2}之间做出选择", "elements": ["character", "choice1", "choice2"]}
            ],
            PlotType.TWIST: [
                {"template": "{character}发现{truth}的真相", "elements": ["character", "truth"]},
                {"template": "{character}原来是{identity}", "elements": ["character", "identity"]},
                {"template": "{event}与预期完全相反", "elements": ["event"]}
            ]
        }

    def _load_conflict_templates(self) -> Dict[ConflictType, List[str]]:
        """加载冲突模板"""
        return {
            ConflictType.MAN_VS_MAN: [
                "{character1}试图阻止{character2}达成目标",
                "{character1}与{character2}争夺{resource}",
                "{character1}与{character2}因{issue}产生分歧"
            ],
            ConflictType.MAN_VS_SELF: [
                "{character}必须克服内心的{fear}",
                "{character}在{choice1}和{choice2}之间挣扎",
                "{character}面临道德困境"
            ],
            ConflictType.MAN_VS_NATURE: [
                "{character}在{environment}中求生",
                "{character}必须对抗{natural_disaster}",
                "{character}穿越{dangerous_terrain}"
            ],
            ConflictType.MAN_VS_SOCIETY: [
                "{character}挑战{social_norm}",
                "{character}与{society}对抗",
                "{character}试图改变{system}"
            ]
        }

    def create_plot_point(
        self,
        plot_id: str,
        plot_type: str,
        description: str,
        act_number: int,
        **kwargs
    ) -> PlotPoint:
        """
        创建情节节点

        Args:
            plot_id: 情节ID
            plot_type: 情节类型
            description: 描述
            act_number: 幕数
            **kwargs: 其他属性

        Returns:
            情节节点
        """
        plot_point = PlotPoint(
            plot_id=plot_id,
            plot_type=PlotType(plot_type),
            description=description,
            act_number=act_number,
            chapter_number=kwargs.get("chapter_number"),
            characters_involved=kwargs.get("characters_involved"),
            location=kwargs.get("location"),
            stakes=kwargs.get("stakes"),
            foreshadowing=kwargs.get("foreshadowing")
        )

        self.plot_points[plot_id] = plot_point
        return plot_point

    def generate_plot_from_template(
        self,
        plot_type: PlotType,
        elements: Dict[str, str],
        act_number: int
    ) -> PlotPoint:
        """
        从模板生成情节

        Args:
            plot_type: 情节类型
            elements: 模板元素
            act_number: 幕数

        Returns:
            情节节点
        """
        templates = self.plot_templates.get(plot_type, [])
        if not templates:
            return None

        template = templates[0]  # 使用第一个模板
        plot_id = f"plot_{len(self.plot_points) + 1}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # 填充模板
        description = template["template"].format(**elements)

        plot_point = self.create_plot_point(
            plot_id=plot_id,
            plot_type=plot_type.value,
            description=description,
            act_number=act_number
        )

        return plot_point

    def create_conflict(
        self,
        conflict_type: str,
        characters: List[str],
        stakes: str,
        location: Optional[str] = None,
        act_number: int = 1
    ) -> PlotPoint:
        """
        创建冲突情节

        Args:
            conflict_type: 冲突类型
            characters: 涉及的角色
            stakes: 赌注
            location: 地点（可选）
            act_number: 幕数

        Returns:
            情节节点
        """
        plot_id = f"conflict_{len(self.plot_points) + 1}"

        templates = self.conflict_templates.get(ConflictType(conflict_type), [])
        if templates:
            template = templates[0]
            # 简单的元素替换
            elements = {
                "character": characters[0] if characters else "某人",
                "character1": characters[0] if len(characters) > 0 else "某人",
                "character2": characters[1] if len(characters) > 1 else "对手",
                "resource": "重要资源",
                "issue": "某个问题",
                "fear": "某种恐惧",
                "choice1": "选择A",
                "choice2": "选择B",
                "challenge": "某种挑战",
                "environment": "恶劣环境",
                "natural_disaster": "自然灾害",
                "dangerous_terrain": "危险地形",
                "social_norm": "社会规范",
                "society": "社会",
                "system": "体制"
            }
            description = template.format(**elements)
        else:
            description = f"冲突发生在{', '.join(characters)}之间"

        plot_point = self.create_plot_point(
            plot_id=plot_id,
            plot_type=PlotType.CONFLICT.value,
            description=description,
            act_number=act_number,
            characters_involved=characters,
            location=location,
            stakes=stakes
        )

        return plot_point

    def add_twist(
        self,
        base_plot_id: str,
        twist_type: str = "revelation",
        foreshadowing_points: Optional[List[str]] = None
    ) -> PlotPoint:
        """
        添加转折

        Args:
            base_plot_id: 基础情节ID
            twist_type: 转折类型
            foreshadowing_points: 伏笔点ID列表

        Returns:
            转折情节节点
        """
        base_plot = self.plot_points.get(base_plot_id)
        if not base_plot:
            return None

        plot_id = f"twist_{len(self.plot_points) + 1}"

        # 生成转折描述
        twist_descriptions = {
            "revelation": f"{base_plot.description}，但真相却出人意料",
            "betrayal": f"{base_plot.description}，然而有人背叛了信任",
            "reversal": f"{base_plot.description}，结果完全相反",
            "identity": f"{base_plot.description}，但某人的身份被揭露"
        }

        description = twist_descriptions.get(
            twist_type,
            f"{base_plot.description}，发生了意想不到的转折"
        )

        plot_point = self.create_plot_point(
            plot_id=plot_id,
            plot_type=PlotType.TWIST.value,
            description=description,
            act_number=base_plot.act_number,
            characters_involved=base_plot.characters_involved.copy(),
            location=base_plot.location,
            foreshadowing=foreshadowing_points or []
        )

        # 添加依赖关系
        plot_point.dependencies.append(base_plot_id)

        return plot_point

    def link_plot_points(self, plot_id1: str, plot_id2: str, relation_type: str = "sequence"):
        """
        连接两个情节节点

        Args:
            plot_id1: 情节1 ID
            plot_id2: 情节2 ID
            relation_type: 关系类型（sequence: 序列, cause_effect: 因果, parallel: 并行）
        """
        plot1 = self.plot_points.get(plot_id1)
        plot2 = self.plot_points.get(plot_id2)

        if plot1 and plot2:
            if plot_id2 not in plot1.dependencies:
                plot1.dependencies.append(plot_id2)

    def get_plot_sequence(self, start_plot_id: Optional[str] = None) -> List[PlotPoint]:
        """
        获取情节序列

        Args:
            start_plot_id: 起始情节ID（可选）

        Returns:
            排序后的情节列表
        """
        if not self.plot_points:
            return []

        # 按幕数和依赖关系排序
        plots = list(self.plot_points.values())

        # 先按幕数排序
        plots.sort(key=lambda x: (x.act_number, x.chapter_number or 0))

        # 处理依赖关系（简化版）
        # 实际应用中可能需要更复杂的拓扑排序
        return plots

    def get_plot_points_by_act(self, act_number: int) -> List[PlotPoint]:
        """获取指定幕的所有情节"""
        return [
            plot for plot in self.plot_points.values()
            if plot.act_number == act_number
        ]

    def get_plot_points_by_character(self, character_name: str) -> List[PlotPoint]:
        """获取涉及指定角色的所有情节"""
        return [
            plot for plot in self.plot_points.values()
            if character_name in plot.characters_involved
        ]

    def update_plot_outcome(self, plot_id: str, outcome: str):
        """
        更新情节结果

        Args:
            plot_id: 情节ID
            outcome: 结果描述
        """
        plot = self.plot_points.get(plot_id)
        if plot:
            plot.outcome = outcome
            plot.completed = True

    def generate_plot_summary(self) -> str:
        """生成情节摘要"""
        if not self.plot_points:
            return "暂无情节点"

        summary_parts = ["## 情节摘要\n"]

        # 按幕分组
        acts = {}
        for plot in self.plot_points.values():
            if plot.act_number not in acts:
                acts[plot.act_number] = []
            acts[plot.act_number].append(plot)

        # 生成摘要
        for act_num in sorted(acts.keys()):
            summary_parts.append(f"### 第 {act_num} 幕")
            for plot in acts[act_num]:
                summary_parts.append(f"- **{plot.plot_type.value}**: {plot.description}")
                if plot.characters_involved:
                    summary_parts.append(f"  涉及角色: {', '.join(plot.characters_involved)}")
                if plot.stakes:
                    summary_parts.append(f"  赌注: {plot.stakes}")
                if plot.outcome:
                    summary_parts.append(f"  结果: {plot.outcome}")
                summary_parts.append("")

        return "\n".join(summary_parts)

    def export_plot(self, filepath: str):
        """
        导出情节到文件

        Args:
            filepath: 文件路径
        """
        data = {
            plot_id: plot.to_dict()
            for plot_id, plot in self.plot_points.items()
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_plot(self, filepath: str):
        """
        从文件加载情节

        Args:
            filepath: 文件路径
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for plot_id, plot_data in data.items():
            self.plot_points[plot_id] = PlotPoint.from_dict(plot_data)

    def clear_plot_points(self):
        """清空所有情节节点"""
        self.plot_points.clear()


# 便捷函数
def create_simple_plot(
    description: str,
    plot_type: str,
    act_number: int = 1
) -> PlotPoint:
    """
    快速创建简单情节

    Args:
        description: 描述
        plot_type: 情节类型
        act_number: 幕数

    Returns:
        情节节点
    """
    generator = PlotGenerator()
    return generator.create_plot_point(
        plot_id=f"simple_plot_{len(generator.plot_points) + 1}",
        plot_type=plot_type,
        description=description,
        act_number=act_number
    )
