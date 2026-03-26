# 快速开始指南

## 🚀 5分钟上手

### 步骤 1: 确认环境

确保你的系统安装了 Python 3.7 或更高版本：

```bash
python --version
```

### 步骤 2: 安装依赖

```bash
pip install -r requirements.txt
```

### 步骤 3: 运行测试

```bash
python test_agent.py
```

你应该看到类似这样的输出：

```
============================================================
创意写作 AI Agent - 快速测试
============================================================

[1/6] 创建 Agent...
✓ Agent 创建成功

[2/6] 初始化项目...
✓ 项目初始化成功

[3/6] 添加角色...
✓ 角色创建成功: 测试角色

[4/6] 添加情节...
✓ 情节添加成功: 测试情节

[5/6] 生成报告...
✓ 报告生成成功
  - 角色: 1 个
  - 情节: 1 个
  - 章节: 3 章

[6/6] 导出项目...
✓ 项目导出成功

============================================================
✅ 所有测试通过！
============================================================
```

### 步骤 4: 运行第一个示例

```bash
python examples/basic_usage.py
```

这会创建一个简单的科幻冒险故事，并生成各种输出文件。

## 📝 创建你的第一个故事

### 方法 1: 使用 Python 代码

创建一个新文件 `my_story.py`：

```python
from creative_writing_agent import CreativeWritingAgent

# 创建 Agent
agent = CreativeWritingAgent()

# 初始化项目
agent.initialize_project(
    theme="我的第一个故事",
    genre="奇幻",
    length="short"
)

# 添加主角
agent.add_character(
    name="小明",
    role="protagonist",
    personality=["勇敢", "善良"],
    background="一个普通的年轻人"
)

# 添加情节
agent.add_plot_point(
    plot_type="inciting_incident",
    description="小明发现了一个神秘的宝箱",
    act_number=1,
    characters_involved=["小明"]
)

# 生成报告
report = agent.generate_project_report()
print(report)

# 导出项目
agent.export_project("my_first_story.json")

print("\n✓ 故事创建完成！")
```

运行它：

```bash
python my_story.py
```

### 方法 2: 使用便捷函数

```python
from creative_writing_agent import create_quick_story

# 快速创建故事
agent = create_quick_story(
    theme="冒险",
    genre="奇幻",
    protagonist_name="勇者",
    antagonist_name="魔王"
)

# 查看结果
print(agent.get_plot_summary())
```

## 🎨 探索更多功能

### 角色管理

```python
from creative_writing_agent import CharacterManager

manager = CharacterManager()

# 创建详细的角色
character = manager.create_character(
    name="张三",
    role="protagonist",
    age=25,
    gender="男",
    appearance="中等身高，黑发",
    personality=["聪明", "勇敢", "有点冲动"],
    background="一个寻找真相的年轻人",
    goals=["找到失踪的父亲", "证明自己的能力"],
    fears=["孤独", "失败"],
    dialogue_style="直接，有时会开玩笑",
    quirks=["思考时会咬笔帽", "喜欢喝咖啡"]
)

# 添加关系
manager.add_relationship("张三", "李四", "朋友", "从小一起长大的朋友")

# 查看角色档案
print(manager.generate_character_profile("张三"))
```

### 情节设计

```python
from creative_writing_agent import PlotGenerator

generator = PlotGenerator()

# 创建情节
plot1 = generator.create_plot_point(
    plot_id="plot_001",
    plot_type="inciting_incident",
    description="主角收到了一封神秘的信",
    act_number=1,
    characters_involved=["主角"],
    stakes="这封信可能改变一切"
)

# 添加冲突
conflict = generator.create_conflict(
    conflict_type="man_vs_man",
    characters=["主角", "反派"],
    stakes="主角的性命危在旦夕",
    act_number=2
)

# 添加转折
twist = generator.add_twist(
    base_plot_id="plot_001",
    twist_type="revelation"
)

# 查看情节摘要
print(generator.generate_plot_summary())
```

### 风格控制

```python
from creative_writing_agent import StyleController

controller = StyleController()

# 应用风格
text = "那天晚上，月亮很亮。"
styled = controller.apply_style(text, WritingStyle.SUSPENSEFUL)
print(styled)

# 模仿作家
mimicked = controller.imitate_author(text, "lu_xun")
print(mimicked)
```

### 情感管理

```python
from creative_writing_agent import EmotionManager

manager = EmotionManager()

# 规划情感弧线
emotion_nodes = manager.plan_emotional_arc(
    character_name="主角",
    arc_type="classic"
)

# 查看情感节点
for node in emotion_nodes:
    print(f"{node.position:.1f}: {node.emotion_type} (强度: {node.intensity.value})")

# 分析情感
analysis = manager.analyze_emotional_arc("主角")
print(f"主导情感: {analysis['dominant_emotion']}")
```

### 伏笔系统

```python
from creative_writing_agent import ForeshadowingSystem

system = ForeshadowingSystem()

# 添加伏笔
foreshadowing = system.create_foreshadowing(
    foreshadowing_id="fs_001",
    foreshadowing_type="object",
    description="一个神秘的怀表",
    content="主角发现了一个旧怀表",
    position=0.1,
    subtlety=4,
    importance=5
)

# 添加呼应
callback = system.create_callback(
    callback_id="cb_001",
    callback_type="direct",
    description="揭示怀表的秘密",
    content="主角明白了怀表的意义",
    position=0.7,
    foreshadowing_ids=["fs_001"]
)

# 分析伏笔
analysis = system.analyze_foreshadowing_effectiveness()
print(f"解决率: {analysis['resolution_rate']}%")
```

## 🔧 集成 LLM

如果你想使用 LLM 来生成内容，可以这样：

```python
from creative_writing_agent import CreativeWritingAgent

# 定义你的 LLM 生成函数
def my_llm_generate(prompt):
    # 这里调用你的 LLM API
    # 例如：OpenAI、Claude、本地模型等
    response = your_llm_api.generate(prompt)
    return response

# 创建 Agent
agent = CreativeWritingAgent(llm_client=my_llm_generate)

# 使用 LLM 生成内容
content = agent.generate_chapter_content(
    chapter_number=1,
    llm_generate_func=my_llm_generate
)

print(content)
```

## 📚 查看示例

运行基础示例：

```bash
python examples/basic_usage.py
```

这将演示：
- ✅ 创建简单故事
- ✅ 角色管理
- ✅ 情节管理
- ✅ 情感弧线
- ✅ 伏笔系统

运行高级示例：

```bash
python examples/advanced_usage.py
```

这将演示：
- ✅ 多角色复杂故事
- ✅ 风格模仿
- ✅ 情感分析
- ✅ 完整工作流

## 🎯 常见任务

### 任务 1: 创建一个短篇故事

```python
agent = CreativeWritingAgent()
agent.initialize_project(theme="冒险", genre="奇幻", length="short")
agent.add_character(name="勇者", role="protagonist", personality=["勇敢"], background="")
agent.add_plot_point(plot_type="inciting_incident", description="勇者踏上了冒险之旅", act_number=1)
agent.export_project("short_story.json")
```

### 任务 2: 创建一个长篇小说

```python
agent = CreativeWritingAgent()
agent.initialize_project(theme="史诗", genre="奇幻", length="long")
# 添加多个角色
agent.add_character(name="主角", role="protagonist", ...)
agent.add_character(name="导师", role="mentor", ...)
agent.add_character(name="反派", role="antagonist", ...)
# 添加复杂情节
for i in range(1, 4):
    agent.add_plot_point(plot_type="rising_action", description=f"情节{i}", act_number=i)
agent.export_project("epic_novel.json")
```

### 任务 3: 分析现有项目

```python
agent = CreativeWritingAgent()
agent.load_project("existing_project.json")

# 生成报告
report = agent.generate_project_report()
print(f"角色: {report['character_count']}")
print(f"情节: {report['plot_point_count']}")

# 查看角色档案
for name in agent.project_state["characters"]:
    print(agent.get_character_profile(name))

# 查看情节摘要
print(agent.get_plot_summary())

# 查看伏笔摘要
print(agent.get_foreshadowing_summary())
```

## 💡 提示和技巧

### 1. 从小项目开始
- 先用短篇模式熟悉系统
- 逐步增加复杂度

### 2. 充分利用模板
- 使用内置的角色模板
- 使用故事结构模板

### 3. 善用导出功能
- 定期导出项目备份
- 使用版本控制管理 JSON 文件

### 4. 集成 LLM 提升效果
- 使用 LLM 生成对话
- 使用 LLM 应用风格

### 5. 分析和优化
- 查看项目报告
- 分析情感弧线
- 检查伏笔解决率

## 🆘 获取帮助

### 查看文档
- README.md - 完整文档
- PROJECT_SUMMARY.md - 项目总结

### 运行示例
- examples/basic_usage.py - 基础示例
- examples/advanced_usage.py - 高级示例

### 运行测试
- test_agent.py - 测试脚本

### 查看代码
- creative_writing_agent/ - 核心代码
- 每个模块都有详细的文档字符串

## 🎉 开始创作吧！

现在你已经准备好了！选择一个你感兴趣的主题，开始你的创作之旅：

```python
from creative_writing_agent import CreativeWritingAgent

# 创建你的故事
agent = CreativeWritingAgent()
agent.initialize_project(
    theme="你的主题",
    genre="你的题材",
    length="short"
)

# 添加角色
agent.add_character(
    name="你的角色名",
    role="protagonist",
    personality=["勇敢", "善良"],
    background="你的背景"
)

# 添加情节
agent.add_plot_point(
    plot_type="inciting_incident",
    description="你的激励事件",
    act_number=1
)

# 导出项目
agent.export_project("your_story.json")

print("✓ 你的故事已创建！")
```

---

**祝你创作愉快！** 🎭📖✨
