import os
import argparse
import time
import re
from file_processor import process_file


def custom_classify(text):
    categories = {
        "a. Personal data": [
            "surname",
            "passport",
            "tax identification",
            "insurance number",
            "phone",
            "email",
            "name",
            "id",
            "sex",
            "age",
            "birth",
        ],
        "b. Credentials for others resources": [
            "username",
            "password",
            "credential",
            "login",
            "authentication",
            "token",
            "code",
            "log",
        ],
        "c. Accounting/HR data": [
            "accounts",
            "human resources",
            "hr department",
            "employee",
            "staff",
            "payroll",
            "salary",
            "wage",
            "benefits",
            "compensation",
            "recruitment",
            "time sheet",
            "attendance",
            "overtime",
        ],
        "d. Financial documents": [
            "invoice",
            "invoices",
            "receipt",
            "receipts",
            "bank payment slip",
            "payment slip",
            "payment order",
            "payment confirmation",
            "bank statement",
            "financial",
            "payment",
            "total",
            "$",
        ],
        "e. Documents marked as confidential": [
            "confidential",
            "classified",
            "private",
            "restricted",
        ],
    }

    # so sanh chu voi categories
    scores = {cat: 0 for cat in categories}
    text_lower = text.lower()
    for cat, keywords in categories.items():
        for keyword in keywords:
            pattern = r"\b" + re.escape(keyword) + r"\b"
            if re.search(pattern, text_lower):
                scores[cat] += 1

    if all(score == 0 for score in scores.values()):
        return "f. Other categories"

    best_category = max(scores, key=scores.get)
    return best_category


def main():
    parser = argparse.ArgumentParser(
        description="English Document Classification Utility"
    )
    parser.add_argument(
        "path",
        type=str,
        nargs="?",
        default="data",
        help="Path to the file or directory to process. Default is the 'data' folder.",
    )
    parser.add_argument("--timeout", type=int, default=300, help="Timeout in seconds")
    args = parser.parse_args()

    start_time = time.time()

    output_file = "results.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("Document Classification Results\n")
        f.write("=" * 50 + "\n\n")

    files_to_process = []
    if os.path.isdir(args.path):
        for root, dirs, files in os.walk(args.path):
            for file in files:
                if file == ".DS_Store":
                    continue
                files_to_process.append(os.path.join(root, file))
    else:
        files_to_process.append(args.path)

    # ghi ket qua vao file results.txt
    for file_path in files_to_process:
        if time.time() - start_time > args.timeout:
            with open(output_file, "a", encoding="utf-8") as f:
                f.write("Timeout exceeded.\n")
            break

        result_text = f"File: {file_path}\n"
        try:
            text = process_file(file_path)
            if text.strip():
                category = custom_classify(text)
                result_text += f"Classification Result: {category}\n"
            else:
                result_text += "No text could be extracted.\n"
        except Exception as e:
            result_text += f"Error processing file: {e}\n"

        result_text += "\n"
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(result_text)


if __name__ == "__main__":
    main()
