"""
创意写作 Agent 基础使用示例
演示如何创建一个简单的故事
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from creative_writing_agent import CreativeWritingAgent


def example_1_create_simple_story():
    """示例1：创建一个简单的故事"""
    print("=" * 60)
    print("示例1：创建一个简单的科幻冒险故事")
    print("=" * 60)

    # 创建 Agent
    agent = CreativeWritingAgent()

    # 初始化项目
    print("\n1. 初始化项目...")
    agent.initialize_project(
        theme="星际探索",
        genre="科幻",
        length="medium",
        structure="three_act"
    )
    print("✓ 项目初始化完成")

    # 添加角色
    print("\n2. 添加角色...")
    protagonist = agent.add_character(
        name="李明",
        role="protagonist",
        personality=["勇敢", "好奇", "聪明"],
        background="一名年轻的宇航员，梦想探索未知星系"
    )
    print(f"✓ 创建主角：{protagonist.name}")

    mentor = agent.add_character(
        name="张教授",
        role="mentor",
        personality=["智慧", "耐心", "神秘"],
        background="资深天文学家，发现了一个神秘的信号"
    )
    print(f"✓ 创建导师：{mentor.name}")

    antagonist = agent.add_character(
        name="暗影",
        role="antagonist",
        personality=["狡猾", "野心勃勃", "无情"],
        background="来自未知文明的神秘存在"
    )
    print(f"✓ 创建反派：{antagonist.name}")

    # 添加角色关系
    print("\n3. 建立角色关系...")
    agent.add_relationship("李明", "张教授", "师生", "李明是张教授的学生")
    agent.add_relationship("李明", "暗影", "敌人", "暗影试图阻止李明的探索")
    print("✓ 角色关系建立完成")

    # 添加情节
    print("\n4. 添加情节节点...")
    agent.add_plot_point(
        plot_type="inciting_incident",
        description="张教授发现了一个来自遥远星系的神秘信号",
        act_number=1,
        characters_involved=["张教授"]
    )
    print("✓ 添加激励事件")

    agent.add_plot_point(
        plot_type="rising_action",
        description="李明被选中前往探索信号的来源",
        act_number=1,
        characters_involved=["李明", "张教授"]
    )
    print("✓ 添加上升动作")

    agent.add_conflict(
        conflict_type="man_vs_fate",
        characters=["李明"],
        stakes="人类的命运悬于一线",
        act_number=2
    )
    print("✓ 添加冲突")

    agent.add_twist(
        base_plot_id=list(agent.plot_generator.plot_points.keys())[0],
        twist_type="revelation"
    )
    print("✓ 添加转折")

    # 添加伏笔
    print("\n5. 添加伏笔...")
    agent.add_foreshadowing(
        foreshadowing_type="object",
        description="一个古老的装置",
        content="张教授在实验室里发现了一个看起来很古老的装置，它似乎在发出微弱的光芒",
        position=0.1,
        subtlety=4,
        importance=5
    )
    print("✓ 添加伏笔")

    # 生成报告
    print("\n6. 生成项目报告...")
    report = agent.generate_project_report()

    print(f"\n故事信息:")
    print(f"  主题: {report['story_info']['theme']}")
    print(f"  题材: {report['story_info']['genre']}")
    print(f"  预计字数: {report['story_info']['estimated_words']} 字")
    print(f"  章节数: {report['chapter_count']}")

    print(f"\n角色统计:")
    print(f"  总数: {report['character_count']}")

    print(f"\n情节点统计:")
    print(f"  总数: {report['plot_point_count']}")
    print(f"  按幕分布: {report['plot_analysis']['by_act']}")

    # 导出项目
    print("\n7. 导出项目...")
    agent.export_project("examples/output/simple_story_project.json")
    print("✓ 项目已导出到 examples/output/simple_story_project.json")

    print("\n" + "=" * 60)
    print("示例1完成！")
    print("=" * 60)


def example_2_character_management():
    """示例2：角色管理"""
    print("\n" + "=" * 60)
    print("示例2：角色管理")
    print("=" * 60)

    from creative_writing_agent import CharacterManager

    # 创建角色管理器
    manager = CharacterManager()

    # 创建角色
    print("\n1. 创建角色...")
    character = manager.create_character(
        name="王小明",
        role="protagonist",
        age=25,
        gender="男",
        appearance="中等身高，黑发，戴眼镜",
        personality=["善良", "勇敢", "有点笨拙"],
        background="一个普通的上班族，喜欢冒险故事",
        goals=["找到真爱", "实现自己的梦想"],
        fears=["孤独", "失败"],
        dialogue_style="真诚，偶尔会开一些笨拙的玩笑",
        quirks=["紧张时会摸鼻子", "喜欢收集旧书"]
    )
    print(f"✓ 创建角色: {character.name}")

    # 添加经历
    print("\n2. 添加角色经历...")
    manager.add_experience(
        character_name="王小明",
        experience="第一次告白被拒绝",
        impact="negative"
    )
    manager.add_experience(
        character_name="王小明",
        experience="帮助陌生人解决了困难",
        impact="positive"
    )
    print("✓ 经历已添加")

    # 角色发展
    print("\n3. 角色发展...")
    manager.develop_character(
        character_name="王小明",
        growth_type="性格改变",
        description="变得更加自信"
    )
    print("✓ 角色已发展")

    # 生成角色档案
    print("\n4. 生成角色档案...")
    profile = manager.generate_character_profile("王小明")
    print(profile)

    # 导出角色
    print("\n5. 导出角色...")
    manager.export_characters("examples/output/characters.json")
    print("✓ 角色已导出到 examples/output/characters.json")

    print("\n" + "=" * 60)
    print("示例2完成！")
    print("=" * 60)


def example_3_plot_management():
    """示例3：情节管理"""
    print("\n" + "=" * 60)
    print("示例3：情节管理")
    print("=" * 60)

    from creative_writing_agent import PlotGenerator

    # 创建情节生成器
    generator = PlotGenerator()

    # 创建情节
    print("\n1. 创建情节节点...")
    plot1 = generator.create_plot_point(
        plot_id="plot_001",
        plot_type="inciting_incident",
        description="主角发现了一封神秘的信件",
        act_number=1,
        characters_involved=["主角"],
        location="主角的家",
        stakes="这封信可能改变一切"
    )
    print(f"✓ 创建情节: {plot1.description}")

    plot2 = generator.create_plot_point(
        plot_id="plot_002",
        plot_type="conflict",
        description="主角在寻找真相的过程中遇到了阻碍",
        act_number=2,
        characters_involved=["主角", "反派"],
        stakes="主角的性命危在旦夕"
    )
    print(f"✓ 创建情节: {plot2.description}")

    # 连接情节
    print("\n2. 连接情节...")
    generator.link_plot_points("plot_001", "plot_002")
    print("✓ 情节已连接")

    # 添加转折
    print("\n3. 添加转折...")
    twist = generator.add_twist(
        base_plot_id="plot_001",
        twist_type="revelation"
    )
    print(f"✓ 添加转折: {twist.description}")

    # 生成情节摘要
    print("\n4. 生成情节摘要...")
    summary = generator.generate_plot_summary()
    print(summary)

    # 导出情节
    print("\n5. 导出情节...")
    generator.export_plot("examples/output/plots.json")
    print("✓ 情节已导出到 examples/output/plots.json")

    print("\n" + "=" * 60)
    print("示例3完成！")
    print("=" * 60)


def example_4_emotion_arc():
    """示例4：情感弧线"""
    print("\n" + "=" * 60)
    print("示例4：情感弧线管理")
    print("=" * 60)

    from creative_writing_agent import EmotionManager

    # 创建情感管理器
    manager = EmotionManager()

    # 创建情感弧线
    print("\n1. 创建经典情感弧线...")
    emotion_nodes = manager.plan_emotional_arc(
        character_name="主角",
        story_length=1.0,
        arc_type="classic"
    )
    print(f"✓ 创建了 {len(emotion_nodes)} 个情感节点")

    # 显示情感节点
    print("\n2. 情感节点列表:")
    for node in emotion_nodes:
        print(f"  位置 {node.position:.1f}: {node.emotion_type} (强度: {node.intensity.value})")
        print(f"    {node.description}")

    # 分析情感弧线
    print("\n3. 分析情感弧线...")
    analysis = manager.analyze_emotional_arc("主角")
    print(f"  主导情感: {analysis['dominant_emotion']}")
    print(f"  平均强度: {analysis['average_intensity']}")
    print(f"  波动性: {analysis['volatility']}")
    print(f"  弧线形状: {analysis['arc_shape']}")

    # 平滑情感曲线
    print("\n4. 平滑情感曲线...")
    smoothed_nodes = manager.smooth_emotional_curve("主角", smoothing_factor=0.3)
    print(f"✓ 平滑后的情感节点数: {len(smoothed_nodes)}")

    # 导出情感数据
    print("\n5. 导出情感数据...")
    manager.export_emotions("examples/output/emotions.json")
    print("✓ 情感数据已导出到 examples/output/emotions.json")

    print("\n" + "=" * 60)
    print("示例4完成！")
    print("=" * 60)


def example_5_foreshadowing():
    """示例5：伏笔与呼应"""
    print("\n" + "=" * 60)
    print("示例5：伏笔与呼应系统")
    print("=" * 60)

    from creative_writing_agent import ForeshadowingSystem

    # 创建伏笔系统
    system = ForeshadowingSystem()

    # 添加伏笔
    print("\n1. 添加伏笔...")
    foreshadowing1 = system.create_foreshadowing(
        foreshadowing_id="fs_001",
        foreshadowing_type="object",
        description="一个神秘的金色怀表",
        content="主角在祖父的遗物中发现了一个金色怀表，表盘上刻着奇怪的符号",
        position=0.1,
        subtlety=3,
        importance=5
    )
    print(f"✓ 添加伏笔: {foreshadowing1.content}")

    foreshadowing2 = system.create_foreshadowing(
        foreshadowing_id="fs_002",
        foreshadowing_type="dialogue",
        description="一句意味深长的话",
        content="祖父临终前对主角说：'当时间停止时，真相就会显现'",
        position=0.15,
        subtlety=4,
        importance=5
    )
    print(f"✓ 添加伏笔: {foreshadowing2.content}")

    # 添加呼应
    print("\n2. 添加呼应...")
    callback1 = system.create_callback(
        callback_id="cb_001",
        callback_type="direct",
        description="揭示怀表的秘密",
        content="主角终于明白了怀表上的符号的含义——它们是一个古老的密码",
        position=0.7,
        foreshadowing_ids=["fs_001"],
        impact=5
    )
    print(f"✓ 添加呼应: {callback1.content}")

    # 生成伏笔摘要
    print("\n3. 生成伏笔摘要...")
    summary = system.generate_foreshadowing_summary()
    print(summary)

    # 分析伏笔有效性
    print("\n4. 分析伏笔有效性...")
    analysis = system.analyze_foreshadowing_effectiveness()
    print(f"  总伏笔数: {analysis['total_foreshadowings']}")
    print(f"  已解决: {analysis['resolved_count']}")
    print(f"  未解决: {analysis['unresolved_count']}")
    print(f"  解决率: {analysis['resolution_rate']}%")

    # 导出伏笔数据
    print("\n5. 导出伏笔数据...")
    system.export_foreshadowings("examples/output/foreshadowings.json")
    print("✓ 伏笔数据已导出到 examples/output/foreshadowings.json")

    print("\n" + "=" * 60)
    print("示例5完成！")
    print("=" * 60)


def main():
    """运行所有示例"""
    print("\n" + "=" * 60)
    print("创意写作 Agent - 基础使用示例")
    print("=" * 60)

    # 创建输出目录
    os.makedirs("examples/output", exist_ok=True)

    # 运行示例
    example_1_create_simple_story()
    example_2_character_management()
    example_3_plot_management()
    example_4_emotion_arc()
    example_5_foreshadowing()

    print("\n" + "=" * 60)
    print("所有示例运行完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
