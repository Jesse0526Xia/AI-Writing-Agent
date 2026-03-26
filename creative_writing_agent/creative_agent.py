"""
创意写作 Agent 主控制器
整合所有模块，提供统一的创作接口
"""

from typing import Dict, List, Optional, Tuple
import json
from datetime import datetime

from .story_engine import StoryEngine, StoryLength, StoryStructure
from .character_manager import CharacterManager, Character, CharacterRole
from .plot_generator import PlotGenerator, PlotPoint, PlotType
from .style_controller import StyleController, WritingStyle, Tone
from .emotion_manager import EmotionManager, EmotionNode
from .foreshadowing_system import ForeshadowingSystem, Foreshadowing, Callback


class CreativeWritingAgent:
    """创意写作 Agent 主控制器"""

    def __init__(self, llm_client=None):
        """
        初始化创意写作 Agent

        Args:
            llm_client: LLM 客户端
        """
        self.llm_client = llm_client

        # 初始化各子系统
        self.story_engine = StoryEngine(llm_client)
        self.character_manager = CharacterManager(llm_client)
        self.plot_generator = PlotGenerator(llm_client)
        self.style_controller = StyleController(llm_client)
        self.emotion_manager = EmotionManager(llm_client)
        self.foreshadowing_system = ForeshadowingSystem(llm_client)

        # 项目状态
        self.project_state = {
            "story_blueprint": None,
            "characters": {},
            "plot_points": {},
            "chapters": [],
            "style_profile": None,
            "generated_content": {}
        }

    def initialize_project(
        self,
        theme: str,
        genre: str,
        length: str = "medium",
        structure: str = "three_act",
        style: Optional[str] = None,
        **kwargs
    ) -> Dict:
        """
        初始化项目

        Args:
            theme: 故事主题
            genre: 故事题材
            length: 篇幅 (short/medium/long)
            structure: 结构 (three_act/hero_journey/kishotenketsu)
            style: 写作风格（可选）
            **kwargs: 其他自定义参数

        Returns:
            项目配置
        """
        # 生成故事蓝图
        self.project_state["story_blueprint"] = self.story_engine.create_story_blueprint(
            theme=theme,
            genre=genre,
            length=StoryLength(length),
            structure=StoryStructure(structure),
            custom_requirements=kwargs
        )

        # 设置风格
        if style:
            self.project_state["style_profile"] = {
                "style": style,
                "tone": kwargs.get("tone", "neutral")
            }

        # 生成章节规划
        blueprint = self.project_state["story_blueprint"]
        self.project_state["chapters"] = self.story_engine.generate_chapter_plan(
            blueprint,
            kwargs.get("chapters_per_act")
        )

        return self.project_state["story_blueprint"]

    def add_character(
        self,
        name: str,
        role: str,
        personality: List[str],
        background: str = "",
        **kwargs
    ) -> Character:
        """
        添加角色

        Args:
            name: 角色名
            role: 角色定位
            personality: 性格特征
            background: 背景故事
            **kwargs: 其他角色属性

        Returns:
            角色对象
        """
        character = self.character_manager.create_character(
            name=name,
            role=role,
            personality=personality,
            background=background,
            **kwargs
        )

        self.project_state["characters"][name] = character

        # 为角色规划情感弧线
        arc_type = kwargs.get("emotion_arc_type", "classic")
        emotion_nodes = self.emotion_manager.plan_emotional_arc(
            character_name=name,
            arc_type=arc_type
        )

        return character

    def add_relationship(
        self,
        character1_name: str,
        character2_name: str,
        relationship_type: str,
        description: str = ""
    ):
        """添加角色关系"""
        self.character_manager.add_relationship(
            character1_name,
            character2_name,
            relationship_type,
            description
        )

    def add_plot_point(
        self,
        plot_type: str,
        description: str,
        act_number: int,
        characters_involved: Optional[List[str]] = None,
        **kwargs
    ) -> PlotPoint:
        """
        添加情节节点

        Args:
            plot_type: 情节类型
            description: 描述
            act_number: 幕数
            characters_involved: 涉及的角色
            **kwargs: 其他属性

        Returns:
            情节节点
        """
        plot_id = f"plot_{len(self.plot_generator.plot_points) + 1}"

        plot_point = self.plot_generator.create_plot_point(
            plot_id=plot_id,
            plot_type=plot_type,
            description=description,
            act_number=act_number,
            characters_involved=characters_involved,
            **kwargs
        )

        self.project_state["plot_points"][plot_id] = plot_point

        return plot_point

    def add_conflict(
        self,
        conflict_type: str,
        characters: List[str],
        stakes: str,
        act_number: int = 1,
        **kwargs
    ) -> PlotPoint:
        """添加冲突情节"""
        conflict_plot = self.plot_generator.create_conflict(
            conflict_type=conflict_type,
            characters=characters,
            stakes=stakes,
            act_number=act_number,
            **kwargs
        )

        self.project_state["plot_points"][conflict_plot.plot_id] = conflict_plot

        return conflict_plot

    def add_twist(
        self,
        base_plot_id: str,
        twist_type: str = "revelation",
        **kwargs
    ) -> PlotPoint:
        """添加转折"""
        twist_plot = self.plot_generator.add_twist(
            base_plot_id=base_plot_id,
            twist_type=twist_type,
            **kwargs
        )

        if twist_plot:
            self.project_state["plot_points"][twist_plot.plot_id] = twist_plot

        return twist_plot

    def add_foreshadowing(
        self,
        foreshadowing_type: str,
        description: str,
        content: str,
        position: float,
        **kwargs
    ) -> Foreshadowing:
        """添加伏笔"""
        foreshadowing_id = f"fs_{len(self.foreshadowing_system.foreshadowings) + 1}"

        foreshadowing = self.foreshadowing_system.create_foreshadowing(
            foreshadowing_id=foreshadowing_id,
            foreshadowing_type=foreshadowing_type,
            description=description,
            content=content,
            position=position,
            **kwargs
        )

        return foreshadowing

    def add_callback(
        self,
        foreshadowing_id: str,
        callback_type: str = "direct",
        **kwargs
    ) -> Callback:
        """添加呼应"""
        callback = self.foreshadowing_system.generate_callback(
            foreshadowing_id=foreshadowing_id,
            callback_type=callback_type,
            llm_generate_func=kwargs.get("llm_generate_func")
        )

        return callback

    def generate_character_dialogue(
        self,
        character_name: str,
        context: str,
        listener_name: Optional[str] = None,
        llm_generate_func: Optional[callable] = None
    ) -> str:
        """生成角色对话"""
        return self.character_manager.generate_dialogue(
            character_name=character_name,
            context=context,
            listener_name=listener_name,
            llm_generate_func=llm_generate_func
        )

    def apply_style_to_text(
        self,
        text: str,
        style: Optional[str] = None,
        llm_generate_func: Optional[callable] = None
    ) -> str:
        """应用风格到文本"""
        if style is None and self.project_state["style_profile"]:
            style = self.project_state["style_profile"]["style"]

        if style:
            return self.style_controller.apply_style(
                text=text,
                style=WritingStyle(style),
                llm_generate_func=llm_generate_func
            )

        return text

    def generate_chapter_content(
        self,
        chapter_number: int,
        llm_generate_func: Optional[callable] = None
    ) -> str:
        """
        生成章节内容

        Args:
            chapter_number: 章节号
            llm_generate_func: LLM 生成函数

        Returns:
            章节内容
        """
        if chapter_number < 1 or chapter_number > len(self.project_state["chapters"]):
            return ""

        chapter = self.project_state["chapters"][chapter_number - 1]

        # 获取该章节的情节
        chapter_plots = [
            plot for plot in self.plot_generator.plot_points.values()
            if plot.chapter_number == chapter_number
        ]

        # 构建章节生成提示
        prompt = self._build_chapter_prompt(chapter, chapter_plots)

        # 生成内容
        if llm_generate_func:
            content = llm_generate_func(prompt)
        else:
            content = self._generate_simple_chapter(chapter, chapter_plots)

        # 应用风格
        content = self.apply_style_to_text(content, llm_generate_func=llm_generate_func)

        # 保存生成的内容
        self.project_state["generated_content"][f"chapter_{chapter_number}"] = content

        return content

    def _build_chapter_prompt(
        self,
        chapter: Dict,
        plots: List[PlotPoint]
    ) -> str:
        """构建章节生成提示"""
        prompt_parts = [
            f"生成第 {chapter['chapter_number']} 章内容",
            f"所属幕：{chapter['act_name']}",
            f"预计字数：{chapter['word_count']} 字",
            "\n情节要点："
        ]

        for plot in plots:
            prompt_parts.append(f"- {plot.description}")

        if chapter.get("characters"):
            prompt_parts.append(f"\n涉及角色：{', '.join(chapter['characters'])}")

        if chapter.get("setting"):
            prompt_parts.append(f"\n场景设置：{chapter['setting']}")

        prompt_parts.append("\n请根据以上信息生成章节内容：")

        return "\n".join(prompt_parts)

    def _generate_simple_chapter(
        self,
        chapter: Dict,
        plots: List[PlotPoint]
    ) -> str:
        """简单的章节生成"""
        parts = [f"## 第 {chapter['chapter_number']} 章"]

        for plot in plots:
            parts.append(f"\n{plot.description}")

        return "\n".join(parts)

    def generate_full_story(
        self,
        llm_generate_func: Optional[callable] = None
    ) -> str:
        """
        生成完整故事

        Args:
            llm_generate_func: LLM 生成函数

        Returns:
            完整故事内容
        """
        story_parts = []
        blueprint = self.project_state["story_blueprint"]

        # 添加标题
        story_parts.append(f"# {blueprint['theme']} - {blueprint['genre']}\n")

        # 生成各章节
        for i in range(len(self.project_state["chapters"])):
            chapter_content = self.generate_chapter_content(
                chapter_number=i + 1,
                llm_generate_func=llm_generate_func
            )
            story_parts.append(chapter_content)

        return "\n\n".join(story_parts)

    def generate_project_report(self) -> Dict:
        """生成项目报告"""
        report = {
            "story_info": self.project_state["story_blueprint"],
            "character_count": len(self.project_state["characters"]),
            "plot_point_count": len(self.project_state["plot_points"]),
            "chapter_count": len(self.project_state["chapters"]),
            "characters": {},
            "plot_analysis": {},
            "emotion_analysis": {},
            "foreshadowing_analysis": {}
        }

        # 角色信息
        for name, character in self.project_state["characters"].items():
            report["characters"][name] = {
                "role": character.role.value,
                "personality": character.personality,
                "arc_progress": character.arc_progress
            }

        # 情节分析
        report["plot_analysis"] = {
            "total_plots": len(self.plot_generator.plot_points),
            "by_act": {},
            "by_type": {}
        }

        for plot in self.plot_generator.plot_points.values():
            # 按幕统计
            act = plot.act_number
            report["plot_analysis"]["by_act"][act] = report["plot_analysis"]["by_act"].get(act, 0) + 1

            # 按类型统计
            ptype = plot.plot_type.value
            report["plot_analysis"]["by_type"][ptype] = report["plot_analysis"]["by_type"].get(ptype, 0) + 1

        # 情感分析
        for character_name in self.project_state["characters"]:
            report["emotion_analysis"][character_name] = self.emotion_manager.analyze_emotional_arc(
                character_name
            )

        # 伏笔分析
        report["foreshadowing_analysis"] = self.foreshadowing_system.analyze_foreshadowing_effectiveness()

        return report

    def export_project(self, filepath: str):
        """
        导出项目

        Args:
            filepath: 文件路径
        """
        project_data = {
            "story_blueprint": self.project_state["story_blueprint"],
            "characters": {
                name: char.to_dict()
                for name, char in self.project_state["characters"].items()
            },
            "plot_points": {
                plot_id: plot.to_dict()
                for plot_id, plot in self.plot_generator.plot_points.items()
            },
            "chapters": self.project_state["chapters"],
            "style_profile": self.project_state["style_profile"],
            "generated_content": self.project_state["generated_content"],
            "emotion_data": {
                "emotion_nodes": {
                    node_id: {
                        "emotion_type": node.emotion_type,
                        "category": node.category.value,
                        "intensity": node.intensity.value,
                        "description": node.description,
                        "position": node.position,
                        "character_name": node.character_name
                    }
                    for node_id, node in self.emotion_manager.emotion_nodes.items()
                }
            },
            "foreshadowing_data": {
                "foreshadowings": {
                    fs_id: {
                        "foreshadowing_type": fs.foreshadowing_type.value,
                        "description": fs.description,
                        "content": fs.content,
                        "position": fs.position,
                        "callback_id": fs.callback_id
                    }
                    for fs_id, fs in self.foreshadowing_system.foreshadowings.items()
                },
                "callbacks": {
                    cb_id: {
                        "callback_type": cb.callback_type.value,
                        "description": cb.description,
                        "content": cb.content,
                        "position": cb.position,
                        "foreshadowing_ids": cb.foreshadowing_ids
                    }
                    for cb_id, cb in self.foreshadowing_system.callbacks.items()
                }
            }
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(project_data, f, ensure_ascii=False, indent=2)

    def load_project(self, filepath: str):
        """
        加载项目

        Args:
            filepath: 文件路径
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            project_data = json.load(f)

        # 恢复故事蓝图
        self.project_state["story_blueprint"] = project_data["story_blueprint"]

        # 恢复角色
        self.project_state["characters"] = {}
        for name, char_data in project_data["characters"].items():
            character = Character.from_dict(char_data)
            self.project_state["characters"][name] = character
            self.character_manager.characters[name] = character

        # 恢复情节
        for plot_id, plot_data in project_data["plot_points"].items():
            plot = PlotPoint.from_dict(plot_data)
            self.plot_generator.plot_points[plot_id] = plot

        # 恢复章节
        self.project_state["chapters"] = project_data["chapters"]

        # 恢复风格配置
        self.project_state["style_profile"] = project_data.get("style_profile")

        # 恢复生成的内容
        self.project_state["generated_content"] = project_data.get("generated_content", {})

        # 恢复情感数据
        # (简化处理，实际需要更完整的恢复逻辑)

        # 恢复伏笔数据
        # (简化处理，实际需要更完整的恢复逻辑)

    def get_character_profile(self, character_name: str) -> str:
        """获取角色档案"""
        return self.character_manager.generate_character_profile(character_name)

    def get_plot_summary(self) -> str:
        """获取情节摘要"""
        return self.plot_generator.generate_plot_summary()

    def get_foreshadowing_summary(self) -> str:
        """获取伏笔摘要"""
        return self.foreshadowing_system.generate_foreshadowing_summary()

    def get_emotion_analysis(self, character_name: str) -> Dict:
        """获取情感分析"""
        return self.emotion_manager.analyze_emotional_arc(character_name)


# 便捷函数
def create_quick_story(
    theme: str,
    genre: str,
    protagonist_name: str,
    antagonist_name: str
) -> CreativeWritingAgent:
    """
    快速创建故事

    Args:
        theme: 故事主题
        genre: 故事题材
        protagonist_name: 主角名
        antagonist_name: 反派名

    Returns:
        创意写作 Agent 实例
    """
    agent = CreativeWritingAgent()

    # 初始化项目
    agent.initialize_project(
        theme=theme,
        genre=genre,
        length="medium"
    )

    # 添加主角
    agent.add_character(
        name=protagonist_name,
        role="protagonist",
        personality=["勇敢", "善良", "坚毅"],
        background="一个普通的年轻人"
    )

    # 添加反派
    agent.add_character(
        name=antagonist_name,
        role="antagonist",
        personality=["狡猾", "野心勃勃", "无情"],
        background="神秘的幕后黑手"
    )

    # 添加基本情节
    agent.add_plot_point(
        plot_type="inciting_incident",
        description=f"{protagonist_name}遇到了意外事件",
        act_number=1,
        characters_involved=[protagonist_name]
    )

    agent.add_plot_point(
        plot_type="climax",
        description=f"{protagonist_name}与{antagonist_name}最终对决",
        act_number=3,
        characters_involved=[protagonist_name, antagonist_name]
    )

    return agent
