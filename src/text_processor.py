import re


def filter_ingredients(tokens):
    """Очищает токены от технического мусора."""
    stop_words = ['тел', 'адрес', 'республика', 'email', 'год', 'гост', 'ту рб', 'онын', 'курамы', 'изготовитель']
    clean_ingredients = []

    for token in tokens:
        token = token.strip()
        if len(token) < 3:
            continue

        # Если в токене есть стоп-слово — игнорируем его
        is_trash = any(word in token for word in stop_words)
        if not is_trash:
            clean_ingredients.append(token)

    return clean_ingredients


def clean_and_split(raw_text):
    """Основной пайплайн очистки текста."""
    text = raw_text.lower()

    # Ищем точку входа (начало состава)
    start_keywords = ['состав:', 'курамы:', 'ингредиенты:', 'сосiаb', 'соспав']
    start_index = -1
    for key in start_keywords:
        if key in text:
            start_index = text.find(key) + len(key)
            break

    # Берем текст после ключевого слова (или весь, если не нашли)
    content = text[start_index:] if start_index != -1 else text

    # Регулярка: оставляем буквы, цифры и запятые
    cleaned = re.sub(r'[^а-яa-z0-9,\s]', '', content)

    # Токенизация по запятым
    raw_tokens = [t.strip() for t in cleaned.split(',')]

    return filter_ingredients(raw_tokens)


if __name__ == "__main__":
    # Тестовый запуск: проверяем логику очистки
    sample = "СОСТАВ: Молоко, сахар, E500. Изготовитель: ООО 'Молоко', тел: 123"
    print("Testing Processor:", clean_and_split(sample))
