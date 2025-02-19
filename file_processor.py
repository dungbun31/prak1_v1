import os
import zipfile
import tempfile
import email
import docx

import py7zr
import rarfile

from pdfminer.high_level import extract_text as pdf_extract_text
from models.ocr import perform_ocr


def process_file(file_path):
    """
    Extract text content from a file. Supported formats:
    txt, docx, pdf, eml, archives (zip, 7z, rar), and image files.
    """
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext in [".docx"]:
        return extract_docx(file_path)
    elif ext in [".pdf"]:
        text = pdf_extract_text(file_path)
        if not text.strip():
            # Nếu PDF chứa hình ảnh, sử dụng OCR.
            text = perform_ocr(file_path)
        return text
    elif ext == ".eml":
        return extract_eml(file_path)
    elif ext in [".zip", ".7z", ".rar"]:
        return extract_archive(file_path)
    elif ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
        return perform_ocr(file_path)
    else:
        return ""


def extract_docx(file_path):
    doc = docx.Document(file_path)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return "\n".join(fullText)


def extract_eml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        msg = email.message_from_file(f)
    parts = []
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                charset = part.get_content_charset() or "utf-8"
                try:
                    parts.append(
                        part.get_payload(decode=True).decode(charset, errors="replace")
                    )
                except Exception:
                    pass
    else:
        charset = msg.get_content_charset() or "utf-8"
        try:
            parts.append(msg.get_payload(decode=True).decode(charset, errors="replace"))
        except Exception:
            pass
    return "\n".join(parts)


def extract_archive(file_path):
    extracted_text = ""
    with tempfile.TemporaryDirectory() as tmpdirname:
        if file_path.endswith(".zip"):
            with zipfile.ZipFile(file_path, "r") as z:
                z.extractall(tmpdirname)
        elif file_path.endswith(".7z"):
            with py7zr.SevenZipFile(file_path, mode="r") as archive:
                archive.extractall(path=tmpdirname)
        elif file_path.endswith(".rar"):
            with rarfile.RarFile(file_path) as rf:
                rf.extractall(tmpdirname)

        # Xử lý đệ quy các file được giải nén.
        for root, dirs, files in os.walk(tmpdirname):
            for f in files:
                full_path = os.path.join(root, f)
                extracted_text += process_file(full_path) + "\n"
    return extracted_text
