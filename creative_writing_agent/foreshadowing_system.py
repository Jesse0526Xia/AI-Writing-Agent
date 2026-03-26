"""
伏笔与呼应系统
负责伏笔植入、呼应生成、线索管理等
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
import json
from dataclasses import dataclass
from datetime import datetime


class ForeshadowingType(Enum):
    """伏笔类型"""
    OBJECT = "object"  # 物品伏笔
    CHARACTER = "character"  # 角色伏笔
    EVENT = "event"  # 事件伏笔
    DIALOGUE = "dialogue"  # 对话伏笔
    SYMBOL = "symbol"  # 象征伏笔
    ATMOSPHERE = "atmosphere"  # 氛围伏笔


class CallbackType(Enum):
    """呼应类型"""
    DIRECT = "direct"  # 直接呼应
    INDIRECT = "indirect"  # 间接呼应
    REVERSAL = "reversal"  # 反转呼应
    DEEPEN = "deepen"  # 深化呼应


@dataclass
class Foreshadowing:
    """伏笔"""
    foreshadowing_id: str
    foreshadowing_type: ForeshadowingType
    description: str
    content: str  # 伏笔内容
    position: float  # 在故事中的位置 (0.0 - 1.0)
    chapter_number: Optional[int] = None
    plot_point_id: Optional[str] = None
    subtlety: int = 3  # 隐蔽程度 (1-5, 1=很明显, 5=很隐蔽)
    importance: int = 3  # 重要程度 (1-5)
    callback_id: Optional[str] = None  # 关联的呼应ID
    created_at: str = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()


@dataclass
class Callback:
    """呼应"""
    callback_id: str
    callback_type: CallbackType
    description: str
    content: str  # 呼应内容
    position: float  # 在故事中的位置 (0.0 - 1.0)
    chapter_number: Optional[int] = None
    plot_point_id: Optional[str] = None
    foreshadowing_ids: List[str] = None  # 关联的伏笔ID列表
    impact: int = 3  # 影响力 (1-5)
    created_at: str = None

    def __post_init__(self):
        if self.foreshadowing_ids is None:
            self.foreshadowing_ids = []
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()


class ForeshadowingSystem:
    """伏笔与呼应系统"""

    def __init__(self, llm_client=None):
        """
        初始化伏笔系统

        Args:
            llm_client: LLM 客户端
        """
        self.llm_client = llm_client
        self.foreshadowings: Dict[str, Foreshadowing] = {}
        self.callbacks: Dict[str, Callback] = {}
        self.foreshadowing_templates = self._load_templates()

    def _load_templates(self) -> Dict:
        """加载伏笔模板"""
        return {
            "object": [
                "一个{object}被{character}小心地收藏起来",
                "{character}注意到{object}有些异常",
                "{object}在故事早期出现，但似乎不起眼"
            ],
            "character": [
                "{character}对{item}表现出异常的兴趣",
                "{character}提到一个神秘的名字",
                "{character}隐瞒了某些事情"
            ],
            "event": [
                "一件{event}意外地改变了局势",
                "某个{event}在早期发生，暗示后来的发展",
                "一个小小的{event}被忽略，但意义重大"
            ],
            "dialogue": [
                "{character}说了一句意味深长的话",
                "对话中提到了一个关键信息",
                "某句话当时听起来普通，后来发现另有深意"
            ]
        }

    def create_foreshadowing(
        self,
        foreshadowing_id: str,
        foreshadowing_type: str,
        description: str,
        content: str,
        position: float,
        **kwargs
    ) -> Foreshadowing:
        """
        创建伏笔

        Args:
            foreshadowing_id: 伏笔ID
            foreshadowing_type: 伏笔类型
            description: 描述
            content: 伏笔内容
            position: 位置 (0.0 - 1.0)
            **kwargs: 其他属性

        Returns:
            伏笔对象
        """
        foreshadowing = Foreshadowing(
            foreshadowing_id=foreshadowing_id,
            foreshadowing_type=ForeshadowingType(foreshadowing_type),
            description=description,
            content=content,
            position=position,
            chapter_number=kwargs.get("chapter_number"),
            plot_point_id=kwargs.get("plot_point_id"),
            subtlety=kwargs.get("subtlety", 3),
            importance=kwargs.get("importance", 3)
        )

        self.foreshadowings[foreshadowing_id] = foreshadowing
        return foreshadowing

    def create_callback(
        self,
        callback_id: str,
        callback_type: str,
        description: str,
        content: str,
        position: float,
        foreshadowing_ids: List[str],
        **kwargs
    ) -> Callback:
        """
        创建呼应

        Args:
            callback_id: 呼应ID
            callback_type: 呼应类型
            description: 描述
            content: 呼应内容
            position: 位置 (0.0 - 1.0)
            foreshadowing_ids: 关联的伏笔ID列表
            **kwargs: 其他属性

        Returns:
            呼应对象
        """
        callback = Callback(
            callback_id=callback_id,
            callback_type=CallbackType(callback_type),
            description=description,
            content=content,
            position=position,
            chapter_number=kwargs.get("chapter_number"),
            plot_point_id=kwargs.get("plot_point_id"),
            foreshadowing_ids=foreshadowing_ids,
            impact=kwargs.get("impact", 3)
        )

        self.callbacks[callback_id] = callback

        # 更新伏笔的呼应ID
        for fs_id in foreshadowing_ids:
            if fs_id in self.foreshadowings:
                self.foreshadowings[fs_id].callback_id = callback_id

        return callback

    def generate_foreshadowing(
        self,
        foreshadowing_type: str,
        elements: Dict[str, str],
        position: float,
        subtlety: int = 3,
        importance: int = 3
    ) -> Foreshadowing:
        """
        生成伏笔

        Args:
            foreshadowing_type: 伏笔类型
            elements: 模板元素
            position: 位置
            subtlety: 隐蔽程度
            importance: 重要程度

        Returns:
            伏笔对象
        """
        templates = self.foreshadowing_templates.get(foreshadowing_type, [])
        if not templates:
            return None

        # 选择模板（简单选择第一个）
        template = templates[0]

        # 填充模板
        content = template.format(**elements)

        foreshadowing_id = f"fs_{len(self.foreshadowings) + 1}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        foreshadowing = self.create_foreshadowing(
            foreshadowing_id=foreshadowing_id,
            foreshadowing_type=foreshadowing_type,
            description=f"基于模板生成的{foreshadowing_type}伏笔",
            content=content,
            position=position,
            subtlety=subtlety,
            importance=importance
        )

        return foreshadowing

    def generate_callback(
        self,
        foreshadowing_id: str,
        callback_type: str = "direct",
        llm_generate_func: Optional[callable] = None
    ) -> Callback:
        """
        为伏笔生成呼应

        Args:
            foreshadowing_id: 伏笔ID
            callback_type: 呼应类型
            llm_generate_func: LLM 生成函数（可选）

        Returns:
            呼应对象
        """
        foreshadowing = self.foreshadowings.get(foreshadowing_id)
        if not foreshadowing:
            return None

        callback_id = f"cb_{len(self.callbacks) + 1}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # 构建呼应提示
        callback_prompt = self._build_callback_prompt(
            foreshadowing,
            callback_type
        )

        # 生成呼应内容
        if llm_generate_func:
            content = llm_generate_func(callback_prompt)
        else:
            content = self._generate_simple_callback(foreshadowing, callback_type)

        callback = self.create_callback(
            callback_id=callback_id,
            callback_type=callback_type,
            description=f"回应伏笔 {foreshadowing_id}",
            content=content,
            position=foreshadowing.position + 0.3,  # 默认在伏笔后30%的位置
            foreshadowing_ids=[foreshadowing_id]
        )

        return callback

    def _build_callback_prompt(
        self,
        foreshadowing: Foreshadowing,
        callback_type: str
    ) -> str:
        """构建呼应提示"""
        type_descriptions = {
            "direct": "直接揭示伏笔的真相",
            "indirect": "间接暗示伏笔的含义",
            "reversal": "反转伏笔的预期",
            "deepen": "深化伏笔的意义"
        }

        prompt = f"""
        伏笔类型：{foreshadowing.foreshadowing_type.value}
        伏笔内容：{foreshadowing.content}
        呼应类型：{callback_type} - {type_descriptions.get(callback_type, '')}

        请生成一个呼应内容，{type_descriptions.get(callback_type, '回应伏笔')}：
        """

        return prompt

    def _generate_simple_callback(
        self,
        foreshadowing: Foreshadowing,
        callback_type: str
    ) -> str:
        """简单的呼应生成"""
        return f"呼应：{foreshadowing.content}"

    def link_foreshadowing_to_callback(
        self,
        foreshadowing_id: str,
        callback_id: str
    ):
        """
        连接伏笔和呼应

        Args:
            foreshadowing_id: 伏笔ID
            callback_id: 呼应ID
        """
        if foreshadowing_id in self.foreshadowings:
            self.foreshadowings[foreshadowing_id].callback_id = callback_id

        if callback_id in self.callbacks:
            if foreshadowing_id not in self.callbacks[callback_id].foreshadowing_ids:
                self.callbacks[callback_id].foreshadowing_ids.append(foreshadowing_id)

    def get_foreshadowings_by_position(
        self,
        start_position: float,
        end_position: float
    ) -> List[Foreshadowing]:
        """
        获取指定位置范围内的伏笔

        Args:
            start_position: 起始位置
            end_position: 结束位置

        Returns:
            伏笔列表
        """
        return [
            fs for fs in self.foreshadowings.values()
            if start_position <= fs.position <= end_position
        ]

    def get_foreshadowings_by_type(
        self,
        foreshadowing_type: str
    ) -> List[Foreshadowing]:
        """获取指定类型的伏笔"""
        return [
            fs for fs in self.foreshadowings.values()
            if fs.foreshadowing_type.value == foreshadowing_type
        ]

    def get_unresolved_foreshadowings(self) -> List[Foreshadowing]:
        """获取未解决的伏笔"""
        return [
            fs for fs in self.foreshadowings.values()
            if fs.callback_id is None
        ]

    def get_callbacks_by_position(
        self,
        start_position: float,
        end_position: float
    ) -> List[Callback]:
        """
        获取指定位置范围内的呼应

        Args:
            start_position: 起始位置
            end_position: 结束位置

        Returns:
            呼应列表
        """
        return [
            cb for cb in self.callbacks.values()
            if start_position <= cb.position <= end_position
        ]

    def analyze_foreshadowing_effectiveness(self) -> Dict:
        """
        分析伏笔有效性

        Returns:
            分析结果
        """
        total_foreshadowings = len(self.foreshadowings)
        resolved_count = sum(1 for fs in self.foreshadowings.values() if fs.callback_id)
        unresolved_count = total_foreshadowings - resolved_count

        # 按重要程度统计
        importance_distribution = {
            level: sum(1 for fs in self.foreshadowings.values() if fs.importance == level)
            for level in range(1, 6)
        }

        # 按隐蔽程度统计
        subtlety_distribution = {
            level: sum(1 for fs in self.foreshadowings.values() if fs.subtlety == level)
            for level in range(1, 6)
        }

        # 按类型统计
        type_distribution = {}
        for fs in self.foreshadowings.values():
            fs_type = fs.foreshadowing_type.value
            type_distribution[fs_type] = type_distribution.get(fs_type, 0) + 1

        # 计算呼应率
        resolution_rate = resolved_count / total_foreshadowings if total_foreshadowings > 0 else 0

        analysis = {
            "total_foreshadowings": total_foreshadowings,
            "resolved_count": resolved_count,
            "unresolved_count": unresolved_count,
            "resolution_rate": round(resolution_rate * 100, 2),
            "importance_distribution": importance_distribution,
            "subtlety_distribution": subtlety_distribution,
            "type_distribution": type_distribution,
            "recommendations": self._generate_recommendations(resolution_rate, unresolved_count)
        }

        return analysis

    def _generate_recommendations(
        self,
        resolution_rate: float,
        unresolved_count: int
    ) -> List[str]:
        """生成改进建议"""
        recommendations = []

        if resolution_rate < 0.5:
            recommendations.append("伏笔解决率较低，建议为更多伏笔添加呼应")

        if unresolved_count > 5:
            recommendations.append(f"有{unresolved_count}个未解决的伏笔，考虑是否需要呼应或删除")

        if unresolved_count == 0:
            recommendations.append("所有伏笔都已解决，可以考虑增加一些长期伏笔")

        return recommendations

    def generate_foreshadowing_summary(self) -> str:
        """生成伏笔摘要"""
        if not self.foreshadowings:
            return "暂无伏笔"

        summary_parts = ["## 伏笔与呼应摘要\n"]

        # 按位置排序
        sorted_foreshadowings = sorted(
            self.foreshadowings.values(),
            key=lambda x: x.position
        )

        summary_parts.append("### 伏笔列表")
        for fs in sorted_foreshadowings:
            status = "✓ 已解决" if fs.callback_id else "✗ 未解决"
            summary_parts.append(
                f"- **{fs.foreshadowing_type.value}** ({status}): {fs.content}\n"
                f"  位置: {fs.position:.2f} | 隐蔽度: {fs.subtlety}/5 | 重要性: {fs.importance}/5"
            )

        if self.callbacks:
            summary_parts.append("\n### 呼应列表")
            sorted_callbacks = sorted(
                self.callbacks.values(),
                key=lambda x: x.position
            )
            for cb in sorted_callbacks:
                foreshadowing_refs = ", ".join(cb.foreshadowing_ids)
                summary_parts.append(
                    f"- **{cb.callback_type.value}**: {cb.content}\n"
                    f"  关联伏笔: {foreshadowing_refs}\n"
                    f"  位置: {cb.position:.2f} | 影响力: {cb.impact}/5"
                )

        return "\n".join(summary_parts)

    def export_foreshadowings(self, filepath: str):
        """
        导出伏笔数据

        Args:
            filepath: 文件路径
        """
        data = {
            "foreshadowings": {
                fs_id: {
                    "foreshadowing_type": fs.foreshadowing_type.value,
                    "description": fs.description,
                    "content": fs.content,
                    "position": fs.position,
                    "chapter_number": fs.chapter_number,
                    "plot_point_id": fs.plot_point_id,
                    "subtlety": fs.subtlety,
                    "importance": fs.importance,
                    "callback_id": fs.callback_id,
                    "created_at": fs.created_at
                }
                for fs_id, fs in self.foreshadowings.items()
            },
            "callbacks": {
                cb_id: {
                    "callback_type": cb.callback_type.value,
                    "description": cb.description,
                    "content": cb.content,
                    "position": cb.position,
                    "chapter_number": cb.chapter_number,
                    "plot_point_id": cb.plot_point_id,
                    "foreshadowing_ids": cb.foreshadowing_ids,
                    "impact": cb.impact,
                    "created_at": cb.created_at
                }
                for cb_id, cb in self.callbacks.items()
            }
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_foreshadowings(self, filepath: str):
        """
        加载伏笔数据

        Args:
            filepath: 文件路径
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.foreshadowings.clear()
        self.callbacks.clear()

        # 加载伏笔
        for fs_id, fs_data in data["foreshadowings"].items():
            foreshadowing = Foreshadowing(
                foreshadowing_id=fs_id,
                foreshadowing_type=ForeshadowingType(fs_data["foreshadowing_type"]),
                description=fs_data["description"],
                content=fs_data["content"],
                position=fs_data["position"],
                chapter_number=fs_data.get("chapter_number"),
                plot_point_id=fs_data.get("plot_point_id"),
                subtlety=fs_data.get("subtlety", 3),
                importance=fs_data.get("importance", 3),
                callback_id=fs_data.get("callback_id"),
                created_at=fs_data.get("created_at")
            )
            self.foreshadowings[fs_id] = foreshadowing

        # 加载呼应
        for cb_id, cb_data in data["callbacks"].items():
            callback = Callback(
                callback_id=cb_id,
                callback_type=CallbackType(cb_data["callback_type"]),
                description=cb_data["description"],
                content=cb_data["content"],
                position=cb_data["position"],
                chapter_number=cb_data.get("chapter_number"),
                plot_point_id=cb_data.get("plot_point_id"),
                foreshadowing_ids=cb_data.get("foreshadowing_ids", []),
                impact=cb_data.get("impact", 3),
                created_at=cb_data.get("created_at")
            )
            self.callbacks[cb_id] = callback


# 便捷函数
def create_simple_foreshadowing(
    content: str,
    foreshadowing_type: str,
    position: float
) -> Foreshadowing:
    """
    快速创建简单伏笔

    Args:
        content: 伏笔内容
        foreshadowing_type: 伏笔类型
        position: 位置

    Returns:
        伏笔对象
    """
    system = ForeshadowingSystem()
    return system.create_foreshadowing(
        foreshadowing_id=f"simple_fs_{len(system.foreshadowings) + 1}",
        foreshadowing_type=foreshadowing_type,
        description="简单伏笔",
        content=content,
        position=position
    )
