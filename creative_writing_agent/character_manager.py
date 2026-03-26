"""
角色管理系统
负责角色的创建、人设设定、对话生成、角色发展等
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
import json
from datetime import datetime


class CharacterRole(Enum):
    """角色定位"""
    PROTAGONIST = "protagonist"  # 主角
    ANTAGONIST = "antagonist"  # 反派
    SUPPORTING = "supporting"  # 配角
    MENTOR = "mentor"  # 导师
    LOVE_INTEREST = "love_interest"  # 恋爱对象
    SIDEKICK = "sidekick"  # 伙伴
    CAMEO = "cameo"  # 客串


class EmotionState(Enum):
    """情绪状态"""
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"
    FEARFUL = "fearful"
    SURPRISED = "surprised"
    DISGUSTED = "disgusted"
    NEUTRAL = "neutral"
    CONFUSED = "confused"
    EXCITED = "excited"
    ANXIOUS = "anxious"


class Character:
    """角色类"""

    def __init__(
        self,
        name: str,
        role: CharacterRole,
        age: Optional[int] = None,
        gender: Optional[str] = None,
        appearance: Optional[str] = None,
        personality: Optional[List[str]] = None,
        background: Optional[str] = None,
        goals: Optional[List[str]] = None,
        fears: Optional[List[str]] = None,
        dialogue_style: Optional[str] = None,
        quirks: Optional[List[str]] = None
    ):
        """
        初始化角色

        Args:
            name: 角色名
            role: 角色定位
            age: 年龄
            gender: 性别
            appearance: 外貌描述
            personality: 性格特征列表
            background: 背景故事
            goals: 目标列表
            fears: 恐惧列表
            dialogue_style: 说话风格
            quirks: 怪癖或习惯
        """
        self.name = name
        self.role = role
        self.age = age
        self.gender = gender
        self.appearance = appearance or ""
        self.personality = personality or []
        self.background = background or ""
        self.goals = goals or []
        self.fears = fears or []
        self.dialogue_style = dialogue_style or ""
        self.quirks = quirks or []

        # 动态属性
        self.current_emotion = EmotionState.NEUTRAL
        self.relationships = {}  # 与其他角色的关系
        self.experiences = []  # 经历的事件
        self.growth_points = []  # 成长点
        self.arc_progress = 0.0  # 角色弧进度 (0.0 - 1.0)

    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "name": self.name,
            "role": self.role.value,
            "age": self.age,
            "gender": self.gender,
            "appearance": self.appearance,
            "personality": self.personality,
            "background": self.background,
            "goals": self.goals,
            "fears": self.fears,
            "dialogue_style": self.dialogue_style,
            "quirks": self.quirks,
            "current_emotion": self.current_emotion.value,
            "relationships": self.relationships,
            "experiences": self.experiences,
            "growth_points": self.growth_points,
            "arc_progress": self.arc_progress
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Character':
        """从字典创建角色"""
        character = cls(
            name=data["name"],
            role=CharacterRole(data["role"]),
            age=data.get("age"),
            gender=data.get("gender"),
            appearance=data.get("appearance"),
            personality=data.get("personality"),
            background=data.get("background"),
            goals=data.get("goals"),
            fears=data.get("fears"),
            dialogue_style=data.get("dialogue_style"),
            quirks=data.get("quirks")
        )
        character.current_emotion = EmotionState(data.get("current_emotion", "neutral"))
        character.relationships = data.get("relationships", {})
        character.experiences = data.get("experiences", [])
        character.growth_points = data.get("growth_points", [])
        character.arc_progress = data.get("arc_progress", 0.0)
        return character


class CharacterManager:
    """角色管理器"""

    def __init__(self, llm_client=None):
        """
        初始化角色管理器

        Args:
            llm_client: LLM 客户端
        """
        self.llm_client = llm_client
        self.characters: Dict[str, Character] = {}
        self.character_templates = self._load_character_templates()

    def _load_character_templates(self) -> Dict:
        """加载角色模板"""
        return {
            "hero": {
                "role": CharacterRole.PROTAGONIST,
                "personality": ["勇敢", "善良", "坚毅"],
                "dialogue_style": "坚定有力，充满希望"
            },
            "villain": {
                "role": CharacterRole.ANTAGONIST,
                "personality": ["狡猾", "野心勃勃", "无情"],
                "dialogue_style": "阴沉，充满威胁"
            },
            "mentor": {
                "role": CharacterRole.MENTOR,
                "personality": ["智慧", "耐心", "神秘"],
                "dialogue_style": "温和，富有哲理"
            },
            "comic_relief": {
                "role": CharacterRole.SUPPORTING,
                "personality": ["幽默", "乐观", "天真"],
                "dialogue_style": "轻松，充满笑话"
            }
        }

    def create_character(
        self,
        name: str,
        role: str,
        **kwargs
    ) -> Character:
        """
        创建角色

        Args:
            name: 角色名
            role: 角色定位
            **kwargs: 其他角色属性

        Returns:
            角色对象
        """
        # 从模板获取默认值
        template = self.character_templates.get(role, {})

        character = Character(
            name=name,
            role=CharacterRole(role),
            age=kwargs.get("age", template.get("age")),
            gender=kwargs.get("gender"),
            appearance=kwargs.get("appearance"),
            personality=kwargs.get("personality", template.get("personality", [])),
            background=kwargs.get("background"),
            goals=kwargs.get("goals", []),
            fears=kwargs.get("fears", []),
            dialogue_style=kwargs.get("dialogue_style", template.get("dialogue_style", "")),
            quirks=kwargs.get("quirks", [])
        )

        self.characters[name] = character
        return character

    def create_character_from_template(
        self,
        template_name: str,
        name: str,
        **customizations
    ) -> Character:
        """
        从模板创建角色

        Args:
            template_name: 模板名称
            name: 角色名
            **customizations: 自定义属性

        Returns:
            角色对象
        """
        template = self.character_templates.get(template_name, {})

        # 合并模板和自定义属性
        character_data = {**template, **customizations}

        return self.create_character(
            name=name,
            role=character_data.get("role", "supporting"),
            **{k: v for k, v in character_data.items() if k != "role"}
        )

    def get_character(self, name: str) -> Optional[Character]:
        """获取角色"""
        return self.characters.get(name)

    def get_all_characters(self) -> List[Character]:
        """获取所有角色"""
        return list(self.characters.values())

    def get_characters_by_role(self, role: str) -> List[Character]:
        """根据角色定位获取角色"""
        role_enum = CharacterRole(role)
        return [char for char in self.characters.values() if char.role == role_enum]

    def set_emotion(self, character_name: str, emotion: str):
        """
        设置角色情绪

        Args:
            character_name: 角色名
            emotion: 情绪
        """
        character = self.get_character(character_name)
        if character:
            character.current_emotion = EmotionState(emotion)

    def add_relationship(
        self,
        character1_name: str,
        character2_name: str,
        relationship_type: str,
        description: str = ""
    ):
        """
        添加角色关系

        Args:
            character1_name: 角色1名
            character2_name: 角色2名
            relationship_type: 关系类型（朋友、敌人、恋人等）
            description: 关系描述
        """
        char1 = self.get_character(character1_name)
        char2 = self.get_character(character2_name)

        if char1 and char2:
            char1.relationships[character2_name] = {
                "type": relationship_type,
                "description": description
            }
            char2.relationships[character1_name] = {
                "type": relationship_type,
                "description": description
            }

    def add_experience(
        self,
        character_name: str,
        experience: str,
        impact: str = "neutral"
    ):
        """
        添加角色经历

        Args:
            character_name: 角色名
            experience: 经历描述
            impact: 影响类型（positive/negative/neutral）
        """
        character = self.get_character(character_name)
        if character:
            character.experiences.append({
                "description": experience,
                "impact": impact,
                "timestamp": datetime.now().isoformat()
            })

    def develop_character(
        self,
        character_name: str,
        growth_type: str,
        description: str
    ):
        """
        角色发展

        Args:
            character_name: 角色名
            growth_type: 成长类型（性格改变、目标改变等）
            description: 发展描述
        """
        character = self.get_character(character_name)
        if character:
            character.growth_points.append({
                "type": growth_type,
                "description": description,
                "timestamp": datetime.now().isoformat()
            })

            # 更新角色弧进度
            character.arc_progress = min(1.0, character.arc_progress + 0.1)

    def generate_dialogue(
        self,
        character_name: str,
        context: str,
        listener_name: Optional[str] = None,
        llm_generate_func: Optional[callable] = None
    ) -> str:
        """
        生成角色对话

        Args:
            character_name: 角色名
            context: 对话上下文
            listener_name: 听者角色名（可选）
            llm_generate_func: LLM 生成函数（可选）

        Returns:
            对话内容
        """
        character = self.get_character(character_name)
        if not character:
            return ""

        # 构建对话提示
        dialogue_prompt = self._build_dialogue_prompt(character, context, listener_name)

        # 如果有 LLM 客户端，使用 LLM 生成
        if llm_generate_func:
            dialogue = llm_generate_func(dialogue_prompt)
        else:
            # 使用简单的规则生成
            dialogue = self._generate_simple_dialogue(character, context)

        return dialogue

    def _build_dialogue_prompt(
        self,
        character: Character,
        context: str,
        listener_name: Optional[str] = None
    ) -> str:
        """构建对话提示"""
        prompt_parts = [
            f"角色：{character.name}",
            f"定位：{character.role.value}",
            f"性格：{', '.join(character.personality)}",
            f"说话风格：{character.dialogue_style}",
            f"当前情绪：{character.current_emotion.value}",
        ]

        if character.quirks:
            prompt_parts.append(f"习惯：{', '.join(character.quirks)}")

        if listener_name:
            listener = self.get_character(listener_name)
            if listener:
                relationship = character.relationships.get(listener_name, {}).get("type", "陌生人")
                prompt_parts.append(f"与{listener_name}的关系：{relationship}")

        prompt_parts.append(f"\n上下文：{context}")
        prompt_parts.append("\n请生成符合角色特征的对话：")

        return "\n".join(prompt_parts)

    def _generate_simple_dialogue(self, character: Character, context: str) -> str:
        """简单对话生成（不使用 LLM）"""
        # 这里可以实现简单的规则生成
        # 实际应用中应该使用 LLM
        return f"[{character.name}]：{context}"

    def generate_character_profile(self, character_name: str) -> str:
        """
        生成角色档案

        Args:
            character_name: 角色名

        Returns:
            角色档案文本
        """
        character = self.get_character(character_name)
        if not character:
            return ""

        profile_parts = [
            f"## 角色档案：{character.name}",
            f"\n**定位**：{character.role.value}",
        ]

        if character.age:
            profile_parts.append(f"**年龄**：{character.age}")
        if character.gender:
            profile_parts.append(f"**性别**：{character.gender}")

        profile_parts.append(f"\n### 外貌")
        profile_parts.append(character.appearance or "未描述")

        profile_parts.append(f"\n### 性格特征")
        for trait in character.personality:
            profile_parts.append(f"- {trait}")

        if character.background:
            profile_parts.append(f"\n### 背景故事")
            profile_parts.append(character.background)

        if character.goals:
            profile_parts.append(f"\n### 目标")
            for goal in character.goals:
                profile_parts.append(f"- {goal}")

        if character.fears:
            profile_parts.append(f"\n### 恐惧")
            for fear in character.fears:
                profile_parts.append(f"- {fear}")

        if character.quirks:
            profile_parts.append(f"\n### 习惯和怪癖")
            for quirk in character.quirks:
                profile_parts.append(f"- {quirk}")

        profile_parts.append(f"\n### 说话风格")
        profile_parts.append(character.dialogue_style or "未定义")

        if character.relationships:
            profile_parts.append(f"\n### 人际关系")
            for other_name, rel in character.relationships.items():
                profile_parts.append(f"- **{other_name}**：{rel['type']} - {rel.get('description', '')}")

        if character.experiences:
            profile_parts.append(f"\n### 重要经历")
            for exp in character.experiences[-5:]:  # 只显示最近5个
                profile_parts.append(f"- {exp['description']}")

        if character.growth_points:
            profile_parts.append(f"\n### 成长轨迹")
            profile_parts.append(f"进度：{int(character.arc_progress * 100)}%")
            for growth in character.growth_points[-5:]:
                profile_parts.append(f"- {growth['type']}: {growth['description']}")

        return "\n".join(profile_parts)

    def export_characters(self, filepath: str):
        """
        导出所有角色到文件

        Args:
            filepath: 文件路径
        """
        data = {
            name: char.to_dict()
            for name, char in self.characters.items()
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_characters(self, filepath: str):
        """
        从文件加载角色

        Args:
            filepath: 文件路径
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for name, char_data in data.items():
            self.characters[name] = Character.from_dict(char_data)

    def update_character_arc(self, character_name: str, progress: float):
        """
        更新角色弧进度

        Args:
            character_name: 角色名
            progress: 进度 (0.0 - 1.0)
        """
        character = self.get_character(character_name)
        if character:
            character.arc_progress = max(0.0, min(1.0, progress))


# 便捷函数
def create_simple_character(
    name: str,
    role: str,
    personality: List[str],
    background: str = ""
) -> Character:
    """
    快速创建简单角色

    Args:
        name: 角色名
        role: 角色定位
        personality: 性格特征
        background: 背景故事

    Returns:
        角色对象
    """
    manager = CharacterManager()
    return manager.create_character(
        name=name,
        role=role,
        personality=personality,
        background=background
    )
