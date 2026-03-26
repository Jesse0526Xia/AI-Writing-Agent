"""
快速测试脚本
验证创意写作 Agent 的基本功能
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from creative_writing_agent import CreativeWritingAgent


def test_basic_functionality():
    """测试基本功能"""
    print("=" * 60)
    print("创意写作 Agent - 快速测试")
    print("=" * 60)

    try:
        # 1. 测试创建 Agent
        print("\n[1/6] 创建 Agent...")
        agent = CreativeWritingAgent()
        print("✓ Agent 创建成功")

        # 2. 测试初始化项目
        print("\n[2/6] 初始化项目...")
        agent.initialize_project(
            theme="测试故事",
            genre="测试",
            length="short"
        )
        print("✓ 项目初始化成功")

        # 3. 测试添加角色
        print("\n[3/6] 添加角色...")
        character = agent.add_character(
            name="测试角色",
            role="protagonist",
            personality=["勇敢", "善良"],
            background="一个测试角色"
        )
        print(f"✓ 角色创建成功: {character.name}")

        # 4. 测试添加情节
        print("\n[4/6] 添加情节...")
        plot = agent.add_plot_point(
            plot_type="inciting_incident",
            description="测试情节",
            act_number=1,
            characters_involved=["测试角色"]
        )
        print(f"✓ 情节添加成功: {plot.description}")

        # 5. 测试生成报告
        print("\n[5/6] 生成报告...")
        report = agent.generate_project_report()
        print(f"✓ 报告生成成功")
        print(f"  - 角色: {report['character_count']} 个")
        print(f"  - 情节: {report['plot_point_count']} 个")
        print(f"  - 章节: {report['chapter_count']} 章")

        # 6. 测试导出项目
        print("\n[6/6] 导出项目...")
        os.makedirs("test_output", exist_ok=True)
        agent.export_project("test_output/test_project.json")
        print("✓ 项目导出成功")

        print("\n" + "=" * 60)
        print("✅ 所有测试通过！")
        print("=" * 60)

        return True

    except Exception as e:
        print(f"\n❌ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_all_modules():
    """测试所有模块"""
    print("\n" + "=" * 60)
    print("模块测试")
    print("=" * 60)

    from creative_writing_agent import (
        StoryEngine,
        CharacterManager,
        PlotGenerator,
        StyleController,
        EmotionManager,
        ForeshadowingSystem
    )

    modules = {
        "StoryEngine": StoryEngine,
        "CharacterManager": CharacterManager,
        "PlotGenerator": PlotGenerator,
        "StyleController": StyleController,
        "EmotionManager": EmotionManager,
        "ForeshadowingSystem": ForeshadowingSystem
    }

    results = {}

    for name, module_class in modules.items():
        try:
            module = module_class()
            results[name] = "✓ 通过"
            print(f"✓ {name} - 通过")
        except Exception as e:
            results[name] = f"✗ 失败: {str(e)}"
            print(f"✗ {name} - 失败: {str(e)}")

    print("\n" + "=" * 60)
    print("模块测试结果:")
    for name, result in results.items():
        print(f"  {name}: {result}")
    print("=" * 60)

    return all("✓" in result for result in results.values())


if __name__ == "__main__":
    print("\n" + "🎭" * 30)
    print("创意写作 AI Agent - 测试套件")
    print("🎭" * 30 + "\n")

    # 运行基本功能测试
    basic_test_passed = test_basic_functionality()

    # 运行模块测试
    module_test_passed = test_all_modules()

    # 总结
    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)
    print(f"基本功能测试: {'✅ 通过' if basic_test_passed else '❌ 失败'}")
    print(f"模块测试: {'✅ 通过' if module_test_passed else '❌ 失败'}")

    if basic_test_passed and module_test_passed:
        print("\n🎉 恭喜！所有测试都通过了！")
        print("\n接下来你可以：")
        print("  1. 运行基础示例: python examples/basic_usage.py")
        print("  2. 运行高级示例: python examples/advanced_usage.py")
        print("  3. 查看 README.md 了解更多功能")
    else:
        print("\n⚠️  部分测试失败，请检查错误信息")

    print("=" * 60 + "\n")
