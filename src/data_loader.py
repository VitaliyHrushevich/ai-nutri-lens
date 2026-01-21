import os
from PIL import Image

# Вместо DATA_PATH = "data/raw_samples" напиши:
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw_samples')


def load_and_check():
    # Проверяем, существует ли папка
    if not os.path.exists(DATA_PATH):
        print(f"Error: Folder {DATA_PATH} not found!")
        return

    files = [f for f in os.listdir(DATA_PATH) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    print(f"Found {len(files)} images: {files}")

    for file_name in files:
        path = os.path.join(DATA_PATH, file_name)
        try:
            with Image.open(path) as img:
                # В 2026 важно логировать разрешение для анализа качества OCR
                print(f"✅ Loaded: {file_name} | Resolution: {img.size} | Mode: {img.mode}")
        except Exception as e:
            print(f"❌ Failed to load {file_name}: {e}")

if __name__ == "__main__":
    load_and_check()