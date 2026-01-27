import re
from typing import List


class IngredientProcessor:
    """Processor for cleaning and tokenizing raw OCR text."""

    STOP_WORDS = ['тел', 'адрес', 'республика', 'email', 'год', 'гост', 'ту рб', 'онын', 'курамы', 'изготовитель']
    START_KEYWORDS = ['состав:', 'курамы:', 'ингредиенты:', 'сосiаb', 'соспав']

    def filter_ingredients(self, tokens: List[str]) -> List[str]:
        clean_ingredients = []
        for token in tokens:
            token = token.strip()
            if len(token) < 3: continue
            if not any(word in token.lower() for word in self.STOP_WORDS):
                clean_ingredients.append(token)
        return clean_ingredients

    def clean_and_split(self, raw_text: str) -> List[str]:
        text = raw_text.lower()
        start_index = -1
        for key in self.START_KEYWORDS:
            if key in text:
                start_index = text.find(key) + len(key)
                break
        content = text[start_index:] if start_index != -1 else text
        cleaned = re.sub(r'[^а-яa-z0-9,\s]', '', content)
        raw_tokens = [t.strip() for t in cleaned.split(',')]
        return self.filter_ingredients(raw_tokens)


# For backwards compatibility (if main.py calls the function directly)
def clean_and_split(raw_text: str) -> List[str]:
    processor = IngredientProcessor()
    return processor.clean_and_split(raw_text)
