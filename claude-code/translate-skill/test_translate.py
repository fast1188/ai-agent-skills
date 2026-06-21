"""test_translate.py — translate skill 单元测试
跑法: python test_translate.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from translate import detect_scenario, build_prompt, SCENARIOS, ANTI_AI_RULES  # noqa


class TestDetect(unittest.TestCase):
    def test_doc(self):
        self.assertEqual(detect_scenario("翻译这段文档"), "doc")
        self.assertEqual(detect_scenario("写个报告给我"), "doc")

    def test_mail(self):
        self.assertEqual(detect_scenario("翻译这封邮件"), "mail")
        self.assertEqual(detect_scenario("给客户的回复"), "mail")

    def test_chat(self):
        self.assertEqual(detect_scenario("这段聊天记录"), "chat")
        self.assertEqual(detect_scenario("微信口语对话"), "chat")

    def test_tech(self):
        self.assertEqual(detect_scenario("API 调用失败"), "tech")
        self.assertEqual(detect_scenario("代码报错 log"), "tech")

    def test_lit(self):
        self.assertEqual(detect_scenario("这段小说"), "lit")
        self.assertEqual(detect_scenario("散文节选"), "lit")

    def test_default(self):
        """无匹配默认 mail"""
        self.assertEqual(detect_scenario("hello world"), "mail")


class TestBuildPrompt(unittest.TestCase):
    def test_basic(self):
        prompt = build_prompt("你好", "mail", "en")
        self.assertIn("你好", prompt)
        self.assertIn("en", prompt)
        self.assertIn("mail", prompt)
        # 6 条反 AI 规则都在
        for rule in ANTI_AI_RULES:
            self.assertIn(rule, prompt)

    def test_all_scenarios(self):
        for s in SCENARIOS:
            prompt = build_prompt("test", s, "en")
            self.assertIn(s, prompt)
            self.assertIn("语域:", prompt)
            self.assertIn("人称:", prompt)
            self.assertIn("时态:", prompt)


class TestScenarios(unittest.TestCase):
    def test_all_5_present(self):
        self.assertEqual(set(SCENARIOS.keys()), {"doc", "mail", "chat", "tech", "lit"})

    def test_all_have_required_fields(self):
        for name, cfg in SCENARIOS.items():
            self.assertIn("trigger", cfg)
            self.assertIn("register", cfg)
            self.assertIn("person", cfg)
            self.assertIn("tense", cfg)
            self.assertIn("length_pct", cfg)
            self.assertEqual(len(cfg["length_pct"]), 2)
            self.assertGreater(len(cfg["trigger"]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
