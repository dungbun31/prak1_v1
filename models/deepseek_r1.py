from transformers import pipeline


class DeepSeekR1Classifier:
    def __init__(self, token=None):
        model_id = "deepseek-ai/DeepSeek-R1"
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
        return self.classifier(text)
