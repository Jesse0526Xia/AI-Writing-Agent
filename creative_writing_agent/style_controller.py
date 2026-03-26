"""
风格控制系统
负责文本风格转换、作家风格模仿、语言风格统一等
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
import json
from dataclasses import dataclass


class WritingStyle(Enum):
    """写作风格"""
    SIMPLE = "simple"  # 简洁
    FLOWERY = "flowery"  - 华丽
    HUMOROUS = "humorous"  # 幽默
    DARK = "dark"  # 黑暗
    OPTIMISTIC = "optimistic"  # 乐观
    PESSIMISTIC = "pessimistic"  # 悲观
    MYSTICAL = "mystical"  # 神秘
    ROMANTIC = "romantic"  # 浪漫
    SUSPENSEFUL = "suspenseful"  # 悬疑
    PHILOSOPHICAL = "philosophical"  # 哲理


class Tone(Enum):
    """语调"""
    FORMAL = "formal"  # 正式
    INFORMAL = "informal"  # 非正式
    SARCASTIC = "sarcastic"  # 讽刺
    SINCERE = "sincere"  # 真诚
    IRONIC = "ironic"  - 反讽
    PLAYFUL = "playful"  # 俏皮
    SERIOUS = "serious"  # 严肃
    WHIMSICAL = "whimsical"  # 异想天开


@dataclass
class AuthorProfile:
    """作家档案"""
    name: str
    style: WritingStyle
    tone: Tone
    characteristics: List[str]
    sentence_complexity: str  # simple/medium/complex
    vocabulary_level: str  # basic/advanced/academic
    common_themes: List[str]
    example_phrases: List[str]


class StyleController:
    """风格控制器"""

    def __init__(self, llm_client=None):
        """
        初始化风格控制器

        Args:
            llm_client: LLM 客户端
        """
        self.llm_client = llm_client
        self.author_profiles = self._load_author_profiles()
        self.style_profiles = self._load_style_profiles()

    def _load_author_profiles(self) -> Dict[str, AuthorProfile]:
        """加载作家档案"""
        return {
            "lu_xun": AuthorProfile(
                name="鲁迅",
                style=WritingStyle.DARK,
                tone=Tone.SARCASTIC,
                characteristics=[
                    "批判现实主义",
                    "尖锐犀利",
                    "深刻洞察",
                    "讽刺幽默"
                ],
                sentence_complexity="medium",
                vocabulary_level="advanced",
                common_themes=["社会批判", "人性揭露", "民族反思"],
                example_phrases=[
                    "我向来是不惮以最坏的恶意，来推测中国人的",
                    "横眉冷对千夫指，俯首甘为孺子牛"
                ]
            ),
            "shen_congwen": AuthorProfile(
                name="沈从文",
                style=WritingStyle.ROMANTIC,
                tone=Tone.SINCERE,
                characteristics=[
                    "唯美主义",
                    "诗意表达",
                    "乡土情怀",
                    "纯净自然"
                ],
                sentence_complexity="medium",
                vocabulary_level="advanced",
                common_themes=["湘西风情", "纯真爱情", "人性美好"],
                example_phrases=[
                    "这个人也许永远不回来了，也许明天回来",
                    "我行过许多地方的桥，看过许多次数的云"
                ]
            ),
            "qian_zhongshu": AuthorProfile(
                name="钱钟书",
                style=WritingStyle.HUMOROUS,
                tone=Tone.IRONIC,
                characteristics=[
                    "机智幽默",
                    "博学多才",
                    "讽刺入骨",
                    "比喻精妙"
                ],
                sentence_complexity="complex",
                vocabulary_level="academic",
                common_themes=["知识分子", "婚姻爱情", "社会讽刺"],
                example_phrases=[
                    "婚姻是一座围城，城外的人想进去，城里的人想出来",
                    "天下只有两种人。譬如一串葡萄到手，一种人挑最好的先吃"
                ]
            ),
            "wang_anyi": AuthorProfile(
                name="王安忆",
                style=WritingStyle.FLOWERY,
                tone=Tone.SERIOUS,
                characteristics=[
                    "细腻写实",
                    "城市书写",
                    "女性视角",
                    "历史反思"
                ],
                sentence_complexity="medium",
                vocabulary_level="advanced",
                common_themes=["上海记忆", "女性命运", "时代变迁"],
                example_phrases=[
                    "上海弄堂里的日子，就像一条静静流淌的河",
                    "时间在弄堂里似乎走得很慢"
                ]
            )
        }

    def _load_style_profiles(self) -> Dict[WritingStyle, Dict]:
        """加载风格配置"""
        return {
            WritingStyle.SIMPLE: {
                "description": "简洁明了，直截了当",
                "features": [
                    "短句为主",
                    "避免复杂修饰",
                    "用词精准",
                    "逻辑清晰"
                ],
                "prompt_modifications": [
                    "使用简单的句式",
                    "避免过多的形容词和副词",
                    "直接表达意思"
                ]
            },
            WritingStyle.FLOWERY: {
                "description": "华丽辞藻，优美表达",
                "features": [
                    "丰富的形容词",
                    "生动的比喻",
                    "优美的意象",
                    "诗意化的表达"
                ],
                "prompt_modifications": [
                    "使用丰富的词汇和修辞",
                    "增加描写和细节",
                    "营造优美的意境"
                ]
            },
            WritingStyle.HUMOROUS: {
                "description": "幽默风趣，轻松愉快",
                "features": [
                    "夸张手法",
                    "反讽讽刺",
                    "俏皮话",
                    "出人意料的转折"
                ],
                "prompt_modifications": [
                    "加入幽默元素",
                    "使用夸张和讽刺",
                    "制造轻松愉快的氛围"
                ]
            },
            WritingStyle.DARK: {
                "description": "黑暗深沉，压抑沉重",
                "features": [
                    "阴郁的氛围",
                    "沉重的主题",
                    "残酷的现实",
                    "绝望的情绪"
                ],
                "prompt_modifications": [
                    "营造压抑的氛围",
                    "描写黑暗和残酷",
                    "表达绝望和痛苦"
                ]
            },
            WritingStyle.SUSPENSEFUL: {
                "description": "悬疑紧张，扣人心弦",
                "features": [
                    "节奏紧凑",
                    "悬念迭起",
                    "紧张刺激",
                    "未知恐惧"
                ],
                "prompt_modifications": [
                    "制造紧张感",
                    "设置悬念",
                    "控制节奏"
                ]
            }
        }

    def apply_style(
        self,
        text: str,
        style: WritingStyle,
        tone: Optional[Tone] = None,
        llm_generate_func: Optional[callable] = None
    ) -> str:
        """
        应用风格到文本

        Args:
            text: 原始文本
            style: 写作风格
            tone: 语调（可选）
            llm_generate_func: LLM 生成函数（可选）

        Returns:
            风格化后的文本
        """
        style_profile = self.style_profiles.get(style, self.style_profiles[WritingStyle.SIMPLE])

        # 构建风格转换提示
        style_prompt = self._build_style_prompt(text, style_profile, tone)

        # 使用 LLM 生成或使用简单规则
        if llm_generate_func:
            styled_text = llm_generate_func(style_prompt)
        else:
            styled_text = self._apply_simple_style(text, style)

        return styled_text

    def _build_style_prompt(
        self,
        text: str,
        style_profile: Dict,
        tone: Optional[Tone]
    ) -> str:
        """构建风格转换提示"""
        prompt_parts = [
            f"风格特征：{style_profile['description']}",
            "\n主要特点："
        ]

        for feature in style_profile["features"]:
            prompt_parts.append(f"- {feature}")

        if tone:
            prompt_parts.append(f"\n语调：{tone.value}")

        prompt_parts.extend([
            "\n原始文本：",
            text,
            "\n请按照上述风格重写这段文字："
        ])

        return "\n".join(prompt_parts)

    def _apply_simple_style(self, text: str, style: WritingStyle) -> str:
        """简单的风格应用（不使用 LLM）"""
        # 这里可以实现简单的规则转换
        # 实际应用中应该使用 LLM
        return text

    def imitate_author(
        self,
        text: str,
        author_name: str,
        llm_generate_func: Optional[callable] = None
    ) -> str:
        """
        模仿作家风格

        Args:
            text: 原始文本
            author_name: 作家名
            llm_generate_func: LLM 生成函数（可选）

        Returns:
            模仿风格的文本
        """
        author_profile = self.author_profiles.get(author_name.lower())

        if not author_profile:
            return f"未找到作家 {author_name} 的风格档案"

        # 构建模仿提示
        mimic_prompt = self._build_mimic_prompt(text, author_profile)

        # 使用 LLM 生成
        if llm_generate_func:
            mimicked_text = llm_generate_func(mimic_prompt)
        else:
            mimicked_text = self._apply_simple_mimic(text, author_profile)

        return mimicked_text

    def _build_mimic_prompt(self, text: str, author_profile: AuthorProfile) -> str:
        """构建模仿作家提示"""
        prompt_parts = [
            f"作家：{author_profile.name}",
            f"风格：{author_profile.style.value}",
            f"语调：{author_profile.tone.value}",
            f"句式复杂度：{author_profile.sentence_complexity}",
            f"词汇水平：{author_profile.vocabulary_level}",
            "\n主要特征："
        ]

        for char in author_profile.characteristics:
            prompt_parts.append(f"- {char}")

        if author_profile.common_themes:
            prompt_parts.append("\n常见主题：")
            for theme in author_profile.common_themes:
                prompt_parts.append(f"- {theme}")

        if author_profile.example_phrases:
            prompt_parts.append("\n例句风格：")
            for phrase in author_profile.example_phrases[:2]:  # 只显示前2个
                prompt_parts.append(f"- {phrase}")

        prompt_parts.extend([
            "\n原始文本：",
            text,
            f"\n请用{author_profile.name}的风格重写这段文字："
        ])

        return "\n".join(prompt_parts)

    def _apply_simple_mimic(self, text: str, author_profile: AuthorProfile) -> str:
        """简单的作家模仿（不使用 LLM）"""
        return f"[{author_profile.name}风格] {text}"

    def create_custom_style(
        self,
        name: str,
        description: str,
        features: List[str],
        prompt_modifications: List[str]
    ) -> WritingStyle:
        """
        创建自定义风格

        Args:
            name: 风格名称
            description: 描述
            features: 特征列表
            prompt_modifications: 提示修改列表

        Returns:
            风格枚举值
        """
        # 这里可以扩展为动态创建风格
        # 暂时返回一个默认风格
        return WritingStyle.SIMPLE

    def blend_styles(
        self,
        text: str,
        styles: List[Tuple[WritingStyle, float]],
        llm_generate_func: Optional[callable] = None
    ) -> str:
        """
        混合多种风格

        Args:
            text: 原始文本
            styles: 风格和权重的列表
            llm_generate_func: LLM 生成函数（可选）

        Returns:
            混合风格后的文本
        """
        # 按权重排序
        sorted_styles = sorted(styles, key=lambda x: x[1], reverse=True)

        # 构建混合风格提示
        blend_prompt = self._build_blend_prompt(text, sorted_styles)

        # 使用 LLM 生成
        if llm_generate_func:
            blended_text = llm_generate_func(blend_prompt)
        else:
            blended_text = text

        return blended_text

    def _build_blend_prompt(
        self,
        text: str,
        styles: List[Tuple[WritingStyle, float]]
    ) -> str:
        """构建混合风格提示"""
        prompt_parts = ["请混合以下风格重写这段文字：\n"]

        for i, (style, weight) in enumerate(styles):
            style_profile = self.style_profiles.get(style, self.style_profiles[WritingStyle.SIMPLE])
            prompt_parts.append(
                f"{i+1}. {style.value} (权重: {weight}) - {style_profile['description']}"
            )

        prompt_parts.extend([
            "\n原始文本：",
            text,
            "\n重写后的文本："
        ])

        return "\n".join(prompt_parts)

    def analyze_text_style(self, text: str) -> Dict:
        """
        分析文本风格

        Args:
            text: 待分析的文本

        Returns:
            风格分析结果
        """
        # 这里可以实现简单的风格分析
        # 实际应用中可以使用 NLP 工具或 LLM

        analysis = {
            "style": "unknown",
            "tone": "neutral",
            "sentence_complexity": "medium",
            "vocabulary_level": "basic",
            "characteristics": [],
            "confidence": 0.5
        }

        return analysis

    def get_style_recommendations(self, genre: str, theme: str) -> List[WritingStyle]:
        """
        获取风格推荐

        Args:
            genre: 故事题材
            theme: 故事主题

        Returns:
            推荐的风格列表
        """
        # 基于题材和主题的简单推荐逻辑
        recommendations = []

        if "悬疑" in genre or "惊悚" in genre:
            recommendations.append(WritingStyle.SUSPENSEFUL)

        if "浪漫" in genre or "爱情" in theme:
            recommendations.append(WritingStyle.ROMANTIC)

        if "喜剧" in genre or "幽默" in theme:
            recommendations.append(WritingStyle.HUMOROUS)

        if "悲剧" in genre or "黑暗" in theme:
            recommendations.append(WritingStyle.DARK)

        if not recommendations:
            recommendations.append(WritingStyle.SIMPLE)

        return recommendations

    def export_author_profiles(self, filepath: str):
        """
        导出作家档案

        Args:
            filepath: 文件路径
        """
        data = {
            name: {
                "name": profile.name,
                "style": profile.style.value,
                "tone": profile.tone.value,
                "characteristics": profile.characteristics,
                "sentence_complexity": profile.sentence_complexity,
                "vocabulary_level": profile.vocabulary_level,
                "common_themes": profile.common_themes,
                "example_phrases": profile.example_phrases
            }
            for name, profile in self.author_profiles.items()
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_author_profiles(self, filepath: str):
        """
        加载作家档案

        Args:
            filepath: 文件路径
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.author_profiles = {}
        for name, profile_data in data.items():
            self.author_profiles[name] = AuthorProfile(
                name=profile_data["name"],
                style=WritingStyle(profile_data["style"]),
                tone=Tone(profile_data["tone"]),
                characteristics=profile_data["characteristics"],
                sentence_complexity=profile_data["sentence_complexity"],
                vocabulary_level=profile_data["vocabulary_level"],
                common_themes=profile_data["common_themes"],
                example_phrases=profile_data["example_phrases"]
            )


# 便捷函数
def apply_simple_style(text: str, style: str) -> str:
    """
    快速应用简单风格

    Args:
        text: 原始文本
        style: 风格名称

    Returns:
        风格化文本
    """
    controller = StyleController()
    return controller.apply_style(text, WritingStyle(style))
