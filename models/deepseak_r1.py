from transformers import pipeline


class DeepSeakR1Classifier:
    def __init__(self, token=None):
        """
        Khởi tạo pipeline phân loại văn bản sử dụng mô hình DeepSeek-R1.
        Nếu mô hình này yêu cầu xác thực, bạn có thể cung cấp token thông qua biến token.
        Nếu không tải được mô hình gốc, chương trình sẽ chuyển sang sử dụng mô hình dự phòng.
        """
        model_id = "deepseek-ai/DeepSeek-R1"  # Cập nhật model identifier mới
        try:
            self.classifier = pipeline(
                "text-classification",
                model=model_id,
                truncation=True,
                use_auth_token=token,
            )
        except Exception as e:
            print(f"Lỗi khi tải mô hình '{model_id}': {e}")
            fallback_model = "distilbert-base-uncased-finetuned-sst-2-english"
            print(f"Đang sử dụng mô hình dự phòng: '{fallback_model}'")
            self.classifier = pipeline(
                "text-classification", model=fallback_model, truncation=True
            )

    def classify(self, text):
        """
        Nhận vào một chuỗi văn bản và trả về kết quả phân loại.

        :param text: str, văn bản cần phân loại.
        :return: list, danh sách kết quả với các key 'label' và 'score'.
        """
        return self.classifier(text)
