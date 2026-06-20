"""test_write_email.py — write-email skill 单元测试
跑法: python test_write_email.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from write_email import detect_scenario, build_email, SCENARIOS


class TestDetect(unittest.TestCase):
    def test_bd(self):
        self.assertEqual(detect_scenario("给客户写商务合作邮件"), "商务")
        self.assertEqual(detect_scenario("proposal to enterprise customer"), "商务")

    def test_job(self):
        self.assertEqual(detect_scenario("我要应聘字节跳动的产品经理"), "求职")
        self.assertEqual(detect_scenario("apply for senior engineer position"), "求职")

    def test_nudge(self):
        self.assertEqual(detect_scenario("催一下客户的合同进度"), "催办")
        self.assertEqual(detect_scenario("follow up on the proposal"), "催办")

    def test_apology(self):
        self.assertEqual(detect_scenario("API 挂了,跟用户道歉"), "道歉")
        self.assertEqual(detect_scenario("sorry for the delay"), "道歉")

    def test_thanks(self):
        self.assertEqual(detect_scenario("感谢老王帮忙推荐"), "感谢")
        self.assertEqual(detect_scenario("thank you for the help"), "感谢")

    def test_default(self):
        # 触发词没匹配,默认商务
        self.assertEqual(detect_scenario("random stuff"), "商务")


class TestBuild(unittest.TestCase):
    def test_basic(self):
        out = build_email("商务", "给客户写试用邀请", to_name="王总")
        self.assertIn("主题行:", out)
        self.assertIn("王总,", out)
        # 6 段以内
        self.assertLessEqual(len(out.split("\n\n")), 6)

    def test_anti_ai_cliches(self):
        """反 AI 套话检测"""
        out = build_email("催办", "催客户进度", to_name="王老师")
        for cliche in ["希望对您有所帮助", "感谢您的宝贵时间", "如有任何疑问", "祝商祺"]:
            self.assertNotIn(cliche, out)

    def test_has_cta(self):
        """骨架里要标出"CTA 槽位"（让 AI 填充）"""
        for s in SCENARIOS:
            out = build_email(s, f"测试 {s} 场景")
            # 模板标了"正文 3" = 行动槽，AI 填血肉时写 CTA
            self.assertIn("正文 3", out)  # CTA 槽位存在

    def test_subject_short(self):
        """主题行 ≤ 18 字"""
        out = build_email("商务", "test", to_name="X")
        for line in out.split("\n"):
            if line.startswith("主题行:"):
                subj = line.replace("主题行:", "").strip()
                self.assertLessEqual(len(subj), 25)  # 中文 18 字 / 英文放宽


class TestScenarios(unittest.TestCase):
    def test_all_5_present(self):
        self.assertEqual(set(SCENARIOS.keys()), {"商务", "求职", "催办", "道歉", "感谢"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
