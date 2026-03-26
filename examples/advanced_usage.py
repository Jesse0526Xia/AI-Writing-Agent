"""
创意写作 Agent 高级使用示例
演示更复杂的功能和集成
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from creative_writing_agent import (
    CreativeWritingAgent,
    StoryEngine,
    CharacterManager,
    PlotGenerator,
    StyleController,
    EmotionManager,
    ForeshadowingSystem
)


def example_6_multi_character_story():
    """示例6：多角色复杂故事"""
    print("=" * 60)
    print("示例6：多角色复杂故事")
    print("=" * 60)

    agent = CreativeWritingAgent()

    # 初始化项目 - 长篇小说
    print("\n1. 初始化长篇小说项目...")
    agent.initialize_project(
        theme="都市悬疑",
        genre="悬疑",
        length="long",
        structure="three_act",
        style="suspenseful",
        tone="serious"
    )
    print("✓ 项目初始化完成")

    # 创建多个角色
    print("\n2. 创建角色团队...")
    characters = []

    # 主角
    protagonist = agent.add_character(
        name="陈警官",
        role="protagonist",
        age=35,
        gender="男",
        personality=["敏锐", "执着", "正义"],
        background="一名经验丰富的刑警，曾破获多起大案",
        goals=["找到真相", "保护无辜者"],
        fears=["无法保护重要的人"],
        dialogue_style="简洁有力，善于观察",
        emotion_arc_type="redemptive"
    )
    characters.append(protagonist)
    print(f"✓ 创建主角: {protagonist.name}")

    # 助手
    sidekick = agent.add_character(
        name="小李",
        role="sidekick",
        age=28,
        gender="女",
        personality=["聪明", "细心", "忠诚"],
        background="陈警官的助手，擅长数据分析",
        goals=["协助破案", "证明自己"],
        dialogue_style="条理清晰，注重细节"
    )
    characters.append(sidekick)
    print(f"✓ 创建助手: {sidekick.name}")

    # 导师
    mentor = agent.add_character(
        name="老王",
        role="mentor",
        age=55,
        gender="男",
        personality=["智慧", "神秘", "经验丰富"],
        background="退休的老刑警，陈警官的师父",
        goals=["指导后辈", "弥补过去的遗憾"],
        dialogue_style="温和，富有哲理"
    )
    characters.append(mentor)
    print(f"✓ 创建导师: {mentor.name}")

    # 反派
    antagonist = agent.add_character(
        name="神秘人",
        role="antagonist",
        personality=["狡猾", "冷酷", "高智商"],
        background="身份不明的幕后黑手",
        goals=["实施完美犯罪", "挑战警方"],
        dialogue_style="冷静，充满威胁"
    )
    characters.append(antagonist)
    print(f"✓ 创建反派: {antagonist.name}")

    # 目击者
    witness = agent.add_character(
        name="张大妈",
        role="supporting",
        age=60,
        gender="女",
        personality=["热心", "健谈", "有点唠叨"],
        background="小区的居民，目击了案件",
        goals=["帮助破案", "保护自己"],
        dialogue_style="口语化，亲切"
    )
    characters.append(witness)
    print(f"✓ 创建目击者: {witness.name}")

    # 建立复杂的关系网络
    print("\n3. 建立角色关系网络...")
    agent.add_relationship("陈警官", "小李", "师徒", "陈警官是小李的师父")
    agent.add_relationship("陈警官", "老王", "师徒", "老王是陈警官的师父")
    agent.add_relationship("陈警官", "神秘人", "敌人", "陈警官正在追查神秘人")
    agent.add_relationship("小李", "老王", "尊敬", "小李很尊敬老王")
    agent.add_relationship("陈警官", "张大妈", "相识", "张大妈协助陈警官办案")
    print("✓ 关系网络建立完成")

    # 创建复杂的情节结构
    print("\n4. 创建情节结构...")
    # 第一幕
    agent.add_plot_point(
        plot_type="exposition",
        description="平静的城市夜晚，陈警官正在处理一起普通的盗窃案",
        act_number=1,
        characters_involved=["陈警官", "小李"]
    )

    agent.add_plot_point(
        plot_type="inciting_incident",
        description="张大妈报案称看到了一起可疑的谋杀案",
        act_number=1,
        characters_involved=["张大妈", "陈警官"]
    )

    agent.add_plot_point(
        plot_type="rising_action",
        description="调查发现这起谋杀案与十年前的悬案有关",
        act_number=1,
        characters_involved=["陈警官", "小李", "老王"]
    )

    # 第二幕
    agent.add_plot_point(
        plot_type="conflict",
        description="调查过程中遭遇阻力和威胁",
        act_number=2,
        characters_involved=["陈警官", "神秘人"]
    )

    agent.add_conflict(
        conflict_type="man_vs_man",
        characters=["陈警官", "神秘人"],
        stakes="真相与谎言的较量",
        act_number=2
    )

    agent.add_plot_point(
        plot_type="rising_action",
        description="小李发现关键线索，但遭到袭击",
        act_number=2,
        characters_involved=["小李", "神秘人"]
    )

    agent.add_twist(
        base_plot_id=list(agent.plot_generator.plot_points.keys())[2],
        twist_type="revelation"
    )

    # 第三幕
    agent.add_plot_point(
        plot_type="climax",
        description="陈警官与神秘人最终对决",
        act_number=3,
        characters_involved=["陈警官", "神秘人"]
    )

    agent.add_plot_point(
        plot_type="resolution",
        description="真相大白，案件告破",
        act_number=3,
        characters_involved=["陈警官", "小李", "老王"]
    )

    print("✓ 情节结构创建完成")

    # 添加多条伏笔线
    print("\n5. 添加伏笔线...")
    # 伏笔线1：神秘物品
    agent.add_foreshadowing(
        foreshadowing_type="object",
        description="一块旧怀表",
        content="在案发现场发现了一块旧怀表，指针停在午夜",
        position=0.1,
        subtlety=4,
        importance=5
    )

    # 伏笔线2：神秘对话
    agent.add_foreshadowing(
        foreshadowing_type="dialogue",
        description="神秘电话",
        content="陈警官接到一个神秘电话，对方说：'十年前的账该算了'",
        position=0.15,
        subtlety=3,
        importance=5
    )

    # 伏笔线3：角色伏笔
    agent.add_foreshadowing(
        foreshadowing_type="character",
        description="老王的异常",
        content="老王在听到十年前的案件时表现异常",
        position=0.2,
        subtlety=4,
        importance=4
    )

    print("✓ 伏笔线添加完成")

    # 生成项目报告
    print("\n6. 生成项目报告...")
    report = agent.generate_project_report()

    print(f"\n故事信息:")
    print(f"  主题: {report['story_info']['theme']}")
    print(f"  题材: {report['story_info']['genre']}")
    print(f"  预计字数: {report['story_info']['estimated_words']} 字")

    print(f"\n角色信息:")
    for name, info in report['characters'].items():
        print(f"  {name}: {info['role']}, 进度: {int(info['arc_progress'] * 100)}%")

    print(f"\n情感分析:")
    for name, analysis in report['emotion_analysis'].items():
        print(f"  {name}:")
        print(f"    主导情感: {analysis['dominant_emotion']}")
        print(f"    弧线形状: {analysis['arc_shape']}")

    # 导出项目
    print("\n7. 导出项目...")
    agent.export_project("examples/output/complex_story_project.json")
    print("✓ 项目已导出")

    print("\n" + "=" * 60)
    print("示例6完成！")
    print("=" * 60)


def example_7_style_imitation():
    """示例7：风格模仿"""
    print("\n" + "=" * 60)
    print("示例7：风格模仿")
    print("=" * 60)

    controller = StyleController()

    # 原始文本
    original_text = """
    那天晚上，月亮很亮，照在湖面上，像是一面镜子。
    他坐在湖边，想着过去的事情。
    风吹过，树叶沙沙作响。
    """

    print("\n原始文本:")
    print(original_text)

    # 用不同作家风格重写
    print("\n1. 模仿鲁迅风格...")
    lu_xun_style = controller.imitate_author(original_text, "lu_xun")
    print(lu_xun_style)

    print("\n2. 模仿沈从文风格...")
    shen_congwen_style = controller.imitate_author(original_text, "shen_congwen")
    print(shen_congwen_style)

    print("\n3. 模仿钱钟书风格...")
    qian_zhongshu_style = controller.imitate_author(original_text, "qian_zhongshu")
    print(qian_zhongshu_style)

    # 应用不同写作风格
    print("\n4. 应用悬疑风格...")
    suspenseful_text = controller.apply_style(original_text, WritingStyle.SUSPENSEFUL)
    print(suspenseful_text)

    print("\n5. 应用幽默风格...")
    humorous_text = controller.apply_style(original_text, WritingStyle.HUMOROUS)
    print(humorous_text)

    print("\n" + "=" * 60)
    print("示例7完成！")
    print("=" * 60)


def example_8_emotion_analysis():
    """示例8：情感分析"""
    print("\n" + "=" * 60)
    print("示例8：情感分析与可视化")
    print("=" * 60)

    from creative_writing_agent import EmotionManager

    manager = EmotionManager()

    # 为不同角色创建不同类型的情感弧线
    print("\n1. 为不同角色创建情感弧线...")

    # 主角 - 救赎弧线
    print("  创建主角的情感弧线（救赎类型）...")
    manager.plan_emotional_arc("主角", arc_type="redemptive")

    # 配角 - 喜剧弧线
    print("  创建配角的情感弧线（喜剧类型）...")
    manager.plan_emotional_arc("配角", arc_type="comedy")

    # 反派 - 悲剧弧线
    print("  创建反派的情感弧线（悲剧类型）...")
    manager.plan_emotional_arc("反派", arc_type="tragedy")

    # 分析每个角色的情感
    print("\n2. 分析角色情感...")
    for character_name in ["主角", "配角", "反派"]:
        analysis = manager.analyze_emotional_arc(character_name)
        print(f"\n{character_name}:")
        print(f"  情感节点数: {analysis['total_emotions']}")
        print(f"  主导情感: {analysis['dominant_emotion']}")
        print(f"  主导类别: {analysis['dominant_category']}")
        print(f"  平均强度: {analysis['average_intensity']}")
        print(f"  波动性: {analysis['volatility']}")
        print(f"  弧线形状: {analysis['arc_shape']}")

        # 显示情感分布
        print(f"  情感类别分布:")
        for category, count in analysis['category_distribution'].items():
            if count > 0:
                print(f"    {category}: {count}")

    # 比较不同角色的情感弧线
    print("\n3. 比较不同角色的情感特征...")
    protagonist_analysis = manager.analyze_emotional_arc("主角")
    antagonist_analysis = manager.analyze_emotional_arc("反派")

    print(f"\n主角 vs 反派:")
    print(f"  平均强度: {protagonist_analysis['average_intensity']:.2f} vs {antagonist_analysis['average_intensity']:.2f}")
    print(f"  波动性: {protagonist_analysis['volatility']:.2f} vs {antagonist_analysis['volatility']:.2f}")
    print(f"  弧线形状: {protagonist_analysis['arc_shape']} vs {antagonist_analysis['arc_shape']}")

    # 获取特定位置的情感
    print("\n4. 获取特定位置的情感...")
    position = 0.5
    for character_name in ["主角", "配角", "反派"]:
        emotion = manager.get_emotion_at_position(character_name, position)
        if emotion:
            print(f"  {character_name}在{position:.1f}位置的情感: {emotion.emotion_type} (强度: {emotion.intensity.value})")

    print("\n" + "=" * 60)
    print("示例8完成！")
    print("=" * 60)


def example_9_complete_workflow():
    """示例9：完整工作流"""
    print("\n" + "=" * 60)
    print("示例9：完整创作工作流")
    print("=" * 60)

    agent = CreativeWritingAgent()

    # 步骤1：初始化
    print("\n步骤1: 初始化项目")
    agent.initialize_project(
        theme="成长与友情",
        genre="青春",
        length="medium",
        structure="three_act"
    )

    # 步骤2：创建角色
    print("\n步骤2: 创建角色")
    agent.add_character(
        name="林小雨",
        role="protagonist",
        personality=["善良", "勇敢", "有点内向"],
        background="一个普通的高中生"
    )

    agent.add_character(
        name="张浩",
        role="love_interest",
        personality=["阳光", "热心", "有点冲动"],
        background="林小雨的同学"
    )

    # 步骤3：建立关系
    print("\n步骤3: 建立关系")
    agent.add_relationship("林小雨", "张浩", "朋友", "从同学变成朋友")

    # 步骤4：规划情节
    print("\n步骤4: 规划情节")
    agent.add_plot_point(
        plot_type="inciting_incident",
        description="林小雨和张浩被分配到同一个小组",
        act_number=1,
        characters_involved=["林小雨", "张浩"]
    )

    agent.add_plot_point(
        plot_type="rising_action",
        description="在合作过程中，两人逐渐了解彼此",
        act_number=2,
        characters_involved=["林小雨", "张浩"]
    )

    agent.add_plot_point(
        plot_type="climax",
        description="在关键的比赛中，两人共同面对挑战",
        act_number=3,
        characters_involved=["林小雨", "张浩"]
    )

    # 步骤5：添加情感弧线
    print("\n步骤5: 添加情感弧线")
    # 情感弧线在添加角色时自动创建

    # 步骤6：添加伏笔
    print("\n步骤6: 添加伏笔")
    agent.add_foreshadowing(
        foreshadowing_type="object",
        description="一本旧日记",
        content="林小雨在图书馆发现了一本旧日记",
        position=0.1,
        importance=3
    )

    # 步骤7：生成报告
    print("\n步骤7: 生成项目报告")
    report = agent.generate_project_report()

    print("\n项目概览:")
    print(f"  主题: {report['story_info']['theme']}")
    print(f"  角色: {report['character_count']} 个")
    print(f"  情节: {report['plot_point_count']} 个")
    print(f"  章节: {report['chapter_count']} 章")

    # 步骤8：导出项目
    print("\n步骤8: 导出项目")
    agent.export_project("examples/output/complete_workflow_project.json")

    print("\n✓ 完整工作流演示完成")

    print("\n" + "=" * 60)
    print("示例9完成！")
    print("=" * 60)


def main():
    """运行所有高级示例"""
    print("\n" + "=" * 60)
    print("创意写作 Agent - 高级使用示例")
    print("=" * 60)

    # 创建输出目录
    os.makedirs("examples/output", exist_ok=True)

    # 运行示例
    example_6_multi_character_story()
    example_7_style_imitation()
    example_8_emotion_analysis()
    example_9_complete_workflow()

    print("\n" + "=" * 60)
    print("所有高级示例运行完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
