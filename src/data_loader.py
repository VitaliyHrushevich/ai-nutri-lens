import os
from PIL import Image


def get_image_metadata(img_path):
    # Returns image metadata for quality analysis.
    if not os.path.exists(img_path):
        return None
    try:
        with Image.open(img_path) as img:
            return {
                "size": img.size,
                "mode": img.mode,
                "format": img.format
            }
    except Exception:
        return None


if __name__ == "__main__":
    # Test run: check if the script sees the photo
    test_path = "data/raw_samples/milk_blurry.jpg"
    meta = get_image_metadata(test_path)
    print(f"Test Metadata for {test_path}: {meta}")
