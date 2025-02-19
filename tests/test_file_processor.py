import unittest
import os
import tempfile
from file_processor import process_file


class TestFileProcessor(unittest.TestCase):
    def test_txt_file(self):
        # Tạo file tạm với nội dung mẫu
        with tempfile.NamedTemporaryFile(
            mode="w+", suffix=".txt", delete=False, encoding="utf-8"
        ) as tmp:
            tmp.write("Đây là file test.")
            tmp_path = tmp.name
        text = process_file(tmp_path)
        os.remove(tmp_path)
        self.assertEqual(text.strip(), "Đây là file test.")


if __name__ == "__main__":
    unittest.main()
