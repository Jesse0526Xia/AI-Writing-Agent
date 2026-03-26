"""
故事生成引擎
支持长短篇小说生成，包含多种故事结构模板
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
import json


class StoryLength(Enum):
    """故事篇幅类型"""
    SHORT = "short"  # 短篇 (1000-5000字)
    MEDIUM = "medium"  # 中篇 (5000-20000字)
    LONG = "long"  # 长篇 (20000字以上)
    SERIAL = "serial"  # 连载


class StoryStructure(Enum):
    """故事结构类型"""
    THREE_ACT = "three_act"  # 三幕式
    HERO_JOURNEY = "hero_journey"  # 英雄之旅
    KISHOTENKETSU = "kishotenketsu"  # 起承转合
    SAVE_THE_CAT = "save_the_cat"  # 救猫咪
    FREYTAG = "freytag"  # 弗赖塔格金字塔


class StoryEngine:
    """故事生成引擎"""

    def __init__(self, llm_client=None):
        """
        初始化故事引擎

        Args:
            llm_client: LLM 客户端（如 OpenAI、Claude 等）
        """
        self.llm_client = llm_client
        self.structure_templates = self._load_structure_templates()

    def _load_structure_templates(self) -> Dict[StoryStructure, Dict]:
        """加载故事结构模板"""
        return {
            StoryStructure.THREE_ACT: {
                "name": "三幕式结构",
                "acts": [
                    {
                        "name": "第一幕：铺垫",
                        "percentage": 25,
                        "elements": [
                            "介绍：介绍主角和背景设定",
                            "激励事件：打破日常平衡的事件",
                            "第一转折点：主角决定采取行动"
                        ]
                    },
                    {
                        "name": "第二幕：对抗",
                        "percentage": 50,
                        "elements": [
                            "上升动作：面临各种挑战和障碍",
                            "中点：重要的转折或发现",
                            "第二转折点：最低点或危机时刻"
                        ]
                    },
                    {
                        "name": "第三幕：结局",
                        "percentage": 25,
                        "elements": [
                            "高潮：最终对抗或解决",
                            "结局：新的平衡状态"
                        ]
                    }
                ]
            },
            StoryStructure.HERO_JOURNEY: {
                "name": "英雄之旅",
                "acts": [
                    {
                        "name": "启程",
                        "percentage": 20,
                        "elements": [
                            "平凡世界：英雄的日常生活",
                            "冒险召唤：英雄被召唤开始冒险",
                            "拒绝召唤：英雄最初犹豫",
                            "遇见导师：英雄获得指导",
                            "跨越门槛：英雄正式踏上旅程"
                        ]
                    },
                    {
                        "name": "启蒙",
                        "percentage": 60,
                        "elements": [
                            "试炼、盟友、敌人：英雄遇到各种挑战",
                            "接近洞穴：接近最危险的考验",
                            "磨难：面对最大的恐惧",
                            "奖赏：获得某种力量或物品"
                        ]
                    },
                    {
                        "name": "回归",
                        "percentage": 20,
                        "elements": [
                            "返回之路：带着奖赏返回",
                            "复活：最后的考验",
                            "带着灵药回归：回到平凡世界，带来改变"
                        ]
                    }
                ]
            },
            StoryStructure.KISHOTENKETSU: {
                "name": "起承转合",
                "acts": [
                    {
                        "name": "起",
                        "percentage": 20,
                        "elements": [
                            "介绍：设定场景和角色",
                            "背景：建立故事的基础"
                        ]
                    },
                    {
                        "name": "承",
                        "percentage": 30,
                        "elements": [
                            "发展：展开故事情节",
                            "深化：加深角色关系和冲突"
                        ]
                    },
                    {
                        "name": "转",
                        "percentage": 30,
                        "elements": [
                            "转折：意外的变化或揭示",
                            "高潮：故事达到顶点"
                        ]
                    },
                    {
                        "name": "合",
                        "percentage": 20,
                        "elements": [
                            "解决：处理后续",
                            "结局：收束故事"
                        ]
                    }
                ]
            }
        }

    def create_story_blueprint(
        self,
        theme: str,
        genre: str,
        length: StoryLength,
        structure: StoryStructure = StoryStructure.THREE_ACT,
        custom_requirements: Optional[Dict] = None
    ) -> Dict:
        """
        创建故事蓝图

        Args:
            theme: 故事主题（如：爱情、冒险、悬疑）
            genre: 故事题材（如：科幻、奇幻、现实主义）
            length: 故事篇幅
            structure: 故事结构
            custom_requirements: 自定义要求

        Returns:
            故事蓝图
        """
        # 获取结构模板
        template = self.structure_templates.get(structure, self.structure_templates[StoryStructure.THREE_ACT])

        # 计算各部分的字数
        total_words = self._estimate_word_count(length)
        act_word_counts = self._calculate_act_word_counts(template["acts"], total_words)

        # 生成故事蓝图
        blueprint = {
            "theme": theme,
            "genre": genre,
            "length": length.value,
            "structure": structure.value,
            "estimated_words": total_words,
            "acts": [],
            "custom_requirements": custom_requirements or {}
        }

        # 生成各幕的详细规划
        for i, act_template in enumerate(template["acts"]):
            act_blueprint = {
                "act_number": i + 1,
                "name": act_template["name"],
                "word_count": act_word_counts[i],
                "percentage": act_template["percentage"],
                "elements": act_template["elements"],
                "plot_points": []  # 将由情节生成器填充
            }
            blueprint["acts"].append(act_blueprint)

        return blueprint

    def _estimate_word_count(self, length: StoryLength) -> int:
        """估算总字数"""
        word_ranges = {
            StoryLength.SHORT: (1000, 5000),
            StoryLength.MEDIUM: (5000, 20000),
            StoryLength.LONG: (20000, 100000),
            StoryLength.SERIAL: (50000, 200000)
        }
        min_words, max_words = word_ranges[length]
        return (min_words + max_words) // 2

    def _calculate_act_word_counts(self, acts: List[Dict], total_words: int) -> List[int]:
        """计算各幕的字数"""
        return [int(total_words * act["percentage"] / 100) for act in acts]

    def generate_chapter_plan(
        self,
        blueprint: Dict,
        chapters_per_act: Optional[List[int]] = None
    ) -> List[Dict]:
        """
        生成章节规划

        Args:
            blueprint: 故事蓝图
            chapters_per_act: 每幕的章节数量（默认每幕3章）

        Returns:
            章节规划列表
        """
        if chapters_per_act is None:
            chapters_per_act = [3] * len(blueprint["acts"])

        chapter_plan = []
        current_chapter = 1

        for i, act in enumerate(blueprint["acts"]):
            num_chapters = chapters_per_act[i]
            words_per_chapter = act["word_count"] // num_chapters

            for j in range(num_chapters):
                chapter = {
                    "chapter_number": current_chapter,
                    "act_number": act["act_number"],
                    "act_name": act["name"],
                    "word_count": words_per_chapter,
                    "plot_points": [],
                    "characters": [],
                    "setting": "",
                    "key_events": []
                }
                chapter_plan.append(chapter)
                current_chapter += 1

        return chapter_plan

    def generate_story_summary(
        self,
        blueprint: Dict,
        characters: List[Dict],
        plot_points: List[Dict]
    ) -> str:
        """
        生成故事摘要

        Args:
            blueprint: 故事蓝图
            characters: 角色列表
            plot_points: 情节点列表

        Returns:
            故事摘要
        """
        summary_parts = []

        # 添加基本信息
        summary_parts.append(f"## {blueprint['theme']} - {blueprint['genre']}")
        summary_parts.append(f"预计字数：{blueprint['estimated_words']} 字\n")

        # 添加角色介绍
        summary_parts.append("### 主要角色")
        for char in characters:
            summary_parts.append(f"- **{char['name']}**: {char['role']} - {char['description']}")

        # 添加故事大纲
        summary_parts.append("\n### 故事大纲")
        for act in blueprint["acts"]:
            summary_parts.append(f"\n#### {act['name']}")
            for element in act["elements"]:
                summary_parts.append(f"- {element}")

        # 添加关键情节
        if plot_points:
            summary_parts.append("\n### 关键情节")
            for point in plot_points:
                summary_parts.append(f"- {point['description']}")

        return "\n".join(summary_parts)

    def export_blueprint(self, blueprint: Dict, filepath: str):
        """
        导出故事蓝图到文件

        Args:
            blueprint: 故事蓝图
            filepath: 文件路径
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(blueprint, f, ensure_ascii=False, indent=2)

    def load_blueprint(self, filepath: str) -> Dict:
        """
        从文件加载故事蓝图

        Args:
            filepath: 文件路径

        Returns:
            故事蓝图
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)


# 便捷函数
def create_story(
    theme: str,
    genre: str,
    length: str = "medium",
    structure: str = "three_act"
) -> Dict:
    """
    快速创建故事蓝图

    Args:
        theme: 故事主题
        genre: 故事题材
        length: 篇幅 (short/medium/long)
        structure: 结构 (three_act/hero_journey/kishotenketsu)

    Returns:
        故事蓝图
    """
    engine = StoryEngine()
    return engine.create_story_blueprint(
        theme=theme,
        genre=genre,
        length=StoryLength(length),
        structure=StoryStructure(structure)
    )
