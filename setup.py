from setuptools import setup, find_packages

setup(
    name="prak1",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
        "pdfminer.six",
        "python-docx",
        "py7zr",
        "rarfile",
        "pytesseract",
        "Pillow",
        "pdf2image",
    ],
    entry_points={"console_scripts": ["prak1 = main:main"]},
    author="Tên của bạn",
    description="Tiện ích quét, xử lý và phân loại tài liệu sử dụng DeepSeak R1",
)
