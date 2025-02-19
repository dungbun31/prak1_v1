import unittest
from models.deepseak_r1 import DeepSeakR1Classifier


class TestDeepSeakR1Classifier(unittest.TestCase):
    def setUp(self):
        self.classifier = DeepSeakR1Classifier()

    def test_classification(self):
        sample_text = "Ví dụ: Email example@test.com, số điện thoại 0123456789, và tên người: Nguyễn Văn A."
        result = self.classifier.classify(sample_text)
        # Kiểm tra kết quả trả về là một danh sách có phần tử
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        for item in result:
            self.assertIn("label", item)
            self.assertIn("score", item)


if __name__ == "__main__":
    unittest.main()
