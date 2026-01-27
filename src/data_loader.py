"""Data Loader for AI Nutri-Lens."""

from typing import Optional, Dict, Tuple
from pathlib import Path
from PIL import Image


class ImageDataLoader:
    def get_image_metadata(self, image_path: Path) -> Optional[Dict[str, str | Tuple[int, int]]]:
        if not image_path.exists():
            return None
        try:
            with Image.open(image_path) as img:
                return {
                    "size": img.size,
                    "mode": img.mode,
                    "format": img.format
                }
        except Exception:
            return None


def get_image_metadata(img_path: str | Path):
    loader = ImageDataLoader()
    return loader.get_image_metadata(Path(img_path))
