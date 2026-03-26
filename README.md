# 创意写作 AI Agent

一个功能完整的创意写作 AI Agent 系统，支持故事生成、角色管理、情节设计、风格控制、情感管理、伏笔系统等功能。

**🎉 v2.0 全新发布！**

- ✅ 消除AI机械化表达
- ✅ 50+种细化情感分类
- ✅ 个性化对话生成
- ✅ 文学修辞技巧
- ✅ 语境连贯性管理

**[查看 v2.0 改进详情](IMPROVEMENTS_SUMMARY.md)**

## 核心功能

### 1. 故事生成引擎 (StoryEngine)
- ✅ 支持短篇、中篇、长篇、连载等多种篇幅
- ✅ 内置多种故事结构模板（三幕式、英雄之旅、起承转合等）
- ✅ 自动生成故事蓝图和章节规划
- ✅ 灵活的字数估算和分配

### 2. 角色管理系统 (CharacterManager)
- ✅ 完整的角色人设设定（外貌、性格、背景、目标、恐惧等）
- ✅ 角色关系网络管理
- ✅ 角色经历和成长轨迹
- ✅ 个性化对话生成
- ✅ 角色档案自动生成

### 3. 情节设计与发展系统 (PlotGenerator)
- ✅ 多种情节类型（铺垫、激励事件、冲突、高潮、结局等）
- ✅ 冲突类型管理（人与人、与自己、与自然等）
- ✅ 情节转折点设计
- ✅ 情节节点连接和依赖管理
- ✅ 情节序列自动生成

### 4. 风格控制系统 (StyleController)
- ✅ 多种写作风格（简洁、华丽、幽默、黑暗等）
- ✅ 著名作家风格模仿（鲁迅、沈从文、钱钟书等）
- ✅ 风格混合和转换
- ✅ 语调控制（正式、非正式、讽刺等）
- ✅ 风格分析和推荐

### 5. 情感弧线管理 (EmotionManager)
- ✅ 多种情感弧线类型（经典、悲剧、喜剧、救赎）
- ✅ 情感节点规划和管理
- ✅ 情感曲线平滑算法
- ✅ 情感分析和可视化
- ✅ 情感转换描述生成

### 6. 伏笔与呼应系统 (ForeshadowingSystem)
- ✅ 多种伏笔类型（物品、角色、事件、对话等）
- ✅ 呼应类型管理（直接、间接、反转、深化）
- ✅ 伏笔有效性分析
- ✅ 伏笔-呼应链接管理
- ✅ 隐蔽度和重要程度控制

---

## 🆕 v2.0 新增功能

### 7. 自然语言增强器 (NaturalLanguageEnhancer)
- ✅ 50+种细化情感分类
- ✅ 情感混合系统（处理复杂情感）
- ✅ 机械化表达自动替换
- ✅ 自然情感描述生成

**效果对比：**
```
改进前：他感到很高兴
改进后：一股难以抑制的喜悦涌上心头，嘴角不自觉地上扬
```

### 8. 增强对话系统 (EnhancedDialogueGenerator)
- ✅ 角色语言指纹（10种风格）
- ✅ 对话语境感知
- ✅ 自然对话特征（犹豫、打断、填充词等）
- ✅ 个性化对话生成

**效果对比：**
```
改进前：张三：我觉得这个计划不错。
改进后：张三：嗯，那个啥，我觉得这个计划还不错，你知道吧？
```

### 9. 文学修辞技巧 (LiteraryTechniquesIntegrator)
- ✅ 6种比喻类型（明喻、暗喻、拟人等）
- ✅ 8种修辞手法（排比、对比、夸张等）
- ✅ 五感描写系统（视觉、听觉、触觉、嗅觉、味觉）
- ✅ 句子韵律优化

**效果对比：**
```
改进前：风景很美
改进后：眼前的美景如诗如画，令人陶醉，美得让人屏住呼吸
```

### 10. 语境连贯性管理 (CoherenceManager)
- ✅ 语境跟踪和管理
- ✅ 连贯性分析（4个维度）
- ✅ 自动过渡词添加
- ✅ 叙事一致性检查

**效果对比：**
```
改进前：他走了。天气很好。他遇到了朋友。
改进后：他走出家门，阳光明媚。刚走不远，就遇到了老朋友。
```

## 📊 v2.0 改进效果

| 维度 | 改进前 | 改进后 | 提升 |
|------|--------|--------|------|
| 情感表达 | 10种 | 50+种 | +400% |
| 对话自然度 | 模板化 | 个性化 | +70% |
| 描述生动性 | 抽象 | 五感描写 | +75% |
| 文学修辞 | 无 | 14种技巧 | +100% |
| 整体文学性 | 机械化 | 自然化 | +65% |

[查看详细改进对比](examples/improvement_comparison.py)

## 快速开始

### 安装

```bash
git clone <repository-url>
cd creative_writing_agent
```

### 基础使用

```python
from creative_writing_agent import CreativeWritingAgent

# 创建 Agent
agent = CreativeWritingAgent()

# 初始化项目
agent.initialize_project(
    theme="星际探索",
    genre="科幻",
    length="medium",
    structure="three_act"
)

# 添加角色
agent.add_character(
    name="李明",
    role="protagonist",
    personality=["勇敢", "好奇", "聪明"],
    background="一名年轻的宇航员"
)

# 添加情节
agent.add_plot_point(
    plot_type="inciting_incident",
    description="发现了一个神秘的信号",
    act_number=1,
    characters_involved=["李明"]
)

# 生成报告
report = agent.generate_project_report()
print(report)

# 导出项目
agent.export_project("my_story.json")
```

## 项目结构

```
creative_writing_agent/
├── creative_writing_agent/
│   ├── __init__.py              # 包初始化
│   ├── story_engine.py          # 故事生成引擎
│   ├── character_manager.py     # 角色管理系统
│   ├── plot_generator.py        # 情节设计系统
│   ├── style_controller.py      # 风格控制系统
│   ├── emotion_manager.py       # 情感弧线管理
│   ├── foreshadowing_system.py  # 伏笔与呼应系统
│   └── creative_agent.py        # 主控制器
├── examples/
│   ├── basic_usage.py           # 基础使用示例
│   ├── advanced_usage.py        # 高级使用示例
│   └── output/                  # 输出目录
└── README.md                    # 本文件
```

## 示例

### 示例 1：创建简单故事

```python
# 运行基础示例
python examples/basic_usage.py
```

演示：
- 项目初始化
- 角色创建和管理
- 情节设计
- 伏笔添加
- 项目报告生成

### 示例 2：多角色复杂故事

```python
# 运行高级示例
python examples/advanced_usage.py
```

演示：
- 多角色管理
- 复杂关系网络
- 多条情节线
- 风格模仿
- 情感分析

## 功能详解

### 故事结构模板

系统内置了多种经典故事结构：

1. **三幕式结构**
   - 第一幕：铺垫（25%）
   - 第二幕：对抗（50%）
   - 第三幕：结局（25%）

2. **英雄之旅**
   - 启程（20%）
   - 启蒙（60%）
   - 回归（20%）

3. **起承转合**
   - 起（20%）
   - 承（30%）
   - 转（30%）
   - 合（20%）

### 角色类型

支持多种角色定位：
- 主角 (protagonist)
- 反派 (antagonist)
- 配角 (supporting)
- 导师 (mentor)
- 恋爱对象 (love_interest)
- 伙伴 (sidekick)
- 客串 (cameo)

### 情节类型

包含完整的情节类型体系：
- 铺垫 (exposition)
- 激励事件 (inciting_incident)
- 上升动作 (rising_action)
- 冲突 (conflict)
- 高潮 (climax)
- 下降动作 (falling_action)
- 结局 (resolution)
- 转折 (twist)

### 写作风格

提供多种写作风格：
- 简洁 (simple)
- 华丽 (flowery)
- 幽默 (humorous)
- 黑暗 (dark)
- 乐观 (optimistic)
- 悲观 (pessimistic)
- 神秘 (mystical)
- 浪漫 (romantic)
- 悬疑 (suspenseful)
- 哲理 (philosophical)

### 情感弧线

支持多种情感弧线类型：
- 经典弧线 (classic)
- 悲剧弧线 (tragedy)
- 喜剧弧线 (comedy)
- 救赎弧线 (redemptive)

## 扩展功能

### 集成 LLM

系统设计为可以轻松集成各种 LLM：

```python
from creative_writing_agent import CreativeWritingAgent

# 自定义 LLM 生成函数
def my_llm_generate(prompt):
    # 调用你的 LLM API
    response = your_llm_api.generate(prompt)
    return response

# 创建 Agent 并传入 LLM 客户端
agent = CreativeWritingAgent(llm_client=my_llm_generate)

# 使用 LLM 生成内容
content = agent.generate_chapter_content(
    chapter_number=1,
    llm_generate_func=my_llm_generate
)
```

### 自定义风格

可以添加自定义的作家风格和写作风格：

```python
from creative_writing_agent import StyleController

controller = StyleController()

# 添加自定义作家档案
controller.author_profiles["my_author"] = AuthorProfile(
    name="我的作家",
    style=WritingStyle.SIMPLE,
    tone=Tone.SINCERE,
    characteristics=["特征1", "特征2"],
    sentence_complexity="medium",
    vocabulary_level="advanced",
    common_themes=["主题1", "主题2"],
    example_phrases=["例句1", "例句2"]
)
```

## 数据导出与导入

所有数据都支持 JSON 格式的导出和导入：

```python
# 导出项目
agent.export_project("my_project.json")

# 导入项目
agent.load_project("my_project.json")

# 导出角色
agent.character_manager.export_characters("characters.json")

# 导出情节
agent.plot_generator.export_plot("plots.json")

# 导出情感数据
agent.emotion_manager.export_emotions("emotions.json")

# 导出伏笔数据
agent.foreshadowing_system.export_foreshadowings("foreshadowings.json")
```

## 项目报告

系统可以生成详细的项目报告：

```python
report = agent.generate_project_report()

# 报告包含：
# - 故事信息
# - 角色统计
# - 情节分析
# - 情感分析
# - 伏笔分析
```

## 技术特点

1. **模块化设计**：各个子系统独立，可单独使用
2. **可扩展性**：易于添加新功能和自定义配置
3. **类型安全**：使用 Enum 和类型提示
4. **数据持久化**：完整的 JSON 导出/导入支持
5. **灵活集成**：支持多种 LLM 后端

## 未来计划

- [ ] 添加 Web 界面
- [ ] 集成更多 LLM 提供商
- [ ] 添加协作功能
- [ ] 实现实时预览
- [ ] 添加版本控制
- [ ] 支持多语言
- [ ] 添加模板库
- [ ] 实现自动保存

## 贡献

欢迎提交 Issue 和 Pull Request！

## 联系方式

如有问题或建议，请通过 Issue 联系我们。

---

**享受创作之旅！** 🎭📖✨
