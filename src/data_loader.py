import os
from PIL import Image

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw_samples')


def load_and_check():
    # 1. Check if the folder exists
    if not os.path.exists(DATA_PATH):
        print(f"Error: Folder {DATA_PATH} not found!")
        return
    #Create list comprehension by filtering only pictures
    files = [f for f in os.listdir(DATA_PATH) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    print(f"Found {len(files)} images: {files}")

    for file_name in files:
        # 3. Join way folder and name file in one line Paste folder path and file name into one correct line
        path = os.path.join(DATA_PATH, file_name)

        try:
            # 4. Open file via context manager 'with'
            with Image.open(path) as img:
                # 5. Output metadata. img.size returns tuple (width, height)
                print(f"✅ Loaded: {file_name} | Resolution: {img.size} | Mode: {img.mode}")
        except Exception as e:
            print(f"❌ Failed to load {file_name}: {e}")

if __name__ == "__main__":
    load_and_check()
