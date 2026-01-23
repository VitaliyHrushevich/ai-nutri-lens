import easyocr
import os

# Initialize the model globally (once at program launch)
reader = easyocr.Reader(['ru', 'en'])


def extract_text(img_path):
    """Извлекает сырой текст из изображения."""
    if not os.path.exists(img_path):
        return ""
    try:
        # rotation_info=True helps if the text on the jar is vertical
        result = reader.readtext(img_path, detail=0)
        return " ".join(result)
    except Exception as e:
        return f"Error during OCR: {e}"


if __name__ == "__main__":
    # Test run: check only recognition
    test_img = "data/raw_samples/milk_blurry.jpg"
    print("Testing OCR...")
    print(extract_text(test_img)[:200], "...") # Print the first 200 characters

