import os
from src.ocr_engine import extract_text
from src.text_processor import clean_and_split


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
    # Здесь мы превращаем кашу в список токенов
    ingredients = clean_and_split(raw_text)

    # 4. Result Presentation
    print("\n" + "=" * 30)
    print(f"✅ PIPELINE COMPLETE")
    print(f"Found {len(ingredients)} ingredient blocks:")
    for idx, item in enumerate(ingredients):
        print(f"{idx + 1}. {item[:150]}...")  # Показываем начало каждого блока
    print("=" * 30)


if __name__ == "__main__":
    run_nutri_lens()
