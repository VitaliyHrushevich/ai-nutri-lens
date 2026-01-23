import os
from src.ocr_engine import extract_text
from src.text_processor import clean_and_split
from src.ai_analyzer import analyze_ingredients


def run_nutri_lens():
    # 1. Setup paths
    image_file = "data/raw_samples/milk_blurry.jpg"

    if not os.path.exists(image_file):
        print(f"❌ Error: Image {image_file} not found.")
        return

    print(f"--- 🚀 Starting Pipeline for: {image_file} ---")

    # 2. Block: OCR (Extraction)
    raw_text = extract_text(image_file)
    if not raw_text:
        print("❌ Error: OCR failed to extract text.")
        return

    # 3. Block: Text Processor (Cleaning)
    ingredients = clean_and_split(raw_text)

    if not ingredients:
        print("❌ Error: No ingredients found after cleaning.")
        return

    # 4. НОВЫЙ БЛОК: AI Analysis (Ollama)
    # Передаем очищенный список в ИИ
    ai_report = analyze_ingredients(ingredients)

    # 5. Result Presentation
    print("\n" + "=" * 30)
    print("📋 ФИНАЛЬНЫЙ ОТЧЕТ ИИ:")
    print(ai_report)
    print("=" * 30)


if __name__ == "__main__":
    run_nutri_lens()
