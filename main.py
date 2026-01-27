"""AI Nutri-Lens - Main entry point."""

import sys
import os
from pathlib import Path

# 1. Setting paths (for Python to see the src folder)
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR / "src"))

# 2. Imports from new modules
from data_loader import ImageDataLoader
from ocr_engine import OCREngine
from text_processor import IngredientProcessor  # Мы назвали его так
from ai_analyzer import NutriAnalyzer        # Мы назвали его так

def run_nutri_lens(image_filename: str = "milk_blurry.jpg"):
    # Path to image
    image_path = BASE_DIR / "data" / "raw_samples" / image_filename

    print(f"--- 🚀 Starting Pipeline for: {image_path.name} ---")

    # Component initialization
    loader = ImageDataLoader()
    ocr = OCREngine()
    processor = IngredientProcessor()
    analyzer = NutriAnalyzer(model="llama3") # Убедись, что модель llama3 скачана

    # 1. Image verification
    meta = loader.get_image_metadata(image_path)
    if not meta:
        print(f"❌ Image not found at: {image_path}")
        return
    print(f"📸 Image OK: {meta['size']}px, {meta['format']}")

    # 2. OCR
    print("⏳ OCR processing (EasyOCR)...")
    raw_text = ocr.extract_text(image_path)

    # Fallback for demonstration if OCR failed with blurred photo
    if len(raw_text) < 10:
        raw_text = "СОСТАВ: молоко цельное, сахар, сливки, стабилизатор E407, пальмовое масло, эмульгатор"
        print("⚠️  Using FALLBACK text (OCR failed or image too blurry)")
    else:
        print(f"🔤 OCR result: {raw_text[:100]}...")

    # 3. word processing
    ingredients = processor.clean_and_split(raw_text)
    if not ingredients:
        print("❌ No ingredients found in text")
        return
    print(f"🧪 Cleaned list: {', '.join(ingredients[:5])}...")

    # 4. AI analysis (Context injection in Ollama)
    print("🧠 AI is analyzing ingredients via Ollama...")
    ai_report = analyzer.analyze_ingredients(ingredients)

    print("\n" + "=" * 60)
    print("📋 ФИНАЛЬНЫЙ ОТЧЕТ ИИ-NUTRI-LENS:")
    print(ai_report)
    print("=" * 60)


if __name__ == "__main__":
    try:
        run_nutri_lens()
    except Exception as e:
        print(f"🛑 Critical System Error: {e}")
