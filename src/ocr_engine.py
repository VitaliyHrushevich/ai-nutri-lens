import easyocr
import os


# Model initialization is done globally to save resources.

reader = easyocr.Reader(['ru', 'en'])


def extract_text(img_path):

    # Function to extract text from a single image.
    if not os.path.exists(img_path):
        print(f"❌ Error: File not found at {img_path}")
        return ""

    try:
        # detail=0 returns only a list of text lines
        result = reader.readtext(img_path, detail=0)

        # Combine the list of rows into one large row
        full_text = " ".join(result)
        return full_text

    except Exception as e:
        print(f"❌ OCR Error: {e}")
        return ""


if __name__ == "__main__":
    test_img = "data/raw_samples/milk_blurry.jpg"
    text = extract_text(test_img)
    print(f"--- TEST OCR OUTPUT ---\n{text}")
