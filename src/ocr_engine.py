import easyocr
import os

# Инициализируем модель глобально (один раз при запуске программы)
reader = easyocr.Reader(['ru', 'en'])

def extract_text(img_path):
    """Извлекает сырой текст из изображения."""
    if not os.path.exists(img_path):
        return ""
    try:
        # rotation_info=True поможет, если текст на банке вертикальный
        result = reader.readtext(img_path, detail=0)
        return " ".join(result)
    except Exception as e:
        return f"Error during OCR: {e}"

if __name__ == "__main__":
    # Тестовый запуск: проверяем только распознавание
    test_img = "data/raw_samples/milk_blurry.jpg"
    print("Testing OCR...")
    print(extract_text(test_img)[:200], "...") # Печатаем первые 200 символов

