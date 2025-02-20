import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path


def perform_ocr(file_path):
    languages = "eng"
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        try:
            images = convert_from_path(file_path)
            text = ""
            for image in images:
                text += pytesseract.image_to_string(image, lang=languages)
            return text
        except Exception:
            return ""
    elif ext in [".png", ".jpg", ".jpeg", ".bmp", ".tiff"]:
        try:
            image = Image.open(file_path)
            return pytesseract.image_to_string(image, lang=languages)
        except Exception:
            return ""
    else:
        return ""
