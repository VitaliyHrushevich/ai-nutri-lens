"""OCR Engine for AI Nutri-Lens."""

from typing import List
from pathlib import Path
import easyocr


class OCREngine:
    def __init__(self, languages: List[str] = None):
        self.languages = languages or ['ru', 'en']
        self._reader = None

    @property
    def reader(self):
        if self._reader is None:
            self._reader = easyocr.Reader(self.languages, gpu=False)
        return self._reader

    def extract_text(self, image_path: Path) -> str:
        if not image_path.exists():
            return "File not found"
        try:
            result = self.reader.readtext(str(image_path), detail=0)
            text = " ".join(result)
            return text.strip() if text.strip() else "No text detected"
        except Exception as e:
            return f"OCR Error: {str(e)}"


def extract_text(img_path: str | Path) -> str:
    engine = OCREngine()
    return engine.extract_text(Path(img_path))
