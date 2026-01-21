import easyocr
import os

# 1. Инициализация (Скачиваем веса нейросети для русского и английского)
# На собесе скажешь: "I used a pre-trained model with support for Cyrillic and Latin scripts."
reader = easyocr.Reader(['ru', 'en'])


def run_ocr():
    DATA_PATH = "data/raw_samples"
    files = [f for f in os.listdir(DATA_PATH) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

    for file_name in files:
        print(f"\n🔎 Reading text from: {file_name}...")
        img_path = os.path.join(DATA_PATH, file_name)

        # 2. Сам процесс распознавания
        # detail=0 вернет только текст. Если поставить 1, он даст координаты рамок.
        result = reader.readtext(img_path, detail=0)

        # 3. Собираем список строк в один абзац (Raw String)
        full_text = " ".join(result)
        print(f"📝 Extracted Text:\n{full_text}")


if __name__ == "__main__":
    run_ocr()