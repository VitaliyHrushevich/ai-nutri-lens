import re


def filter_ingredients(tokens):
    # Cleans toks from technical waste
    stop_words = ['тел', 'адрес', 'республика', 'email', 'год', 'гост', 'ту рб', 'онын', 'курамы', 'изготовитель']
    clean_ingredients = []

    for token in tokens:
        token = token.strip()
        if len(token) < 3:
            continue

        # If there is a stop-word in the token - ignore it
        is_trash = any(word in token for word in stop_words)
        if not is_trash:
            clean_ingredients.append(token)

    return clean_ingredients


def clean_and_split(raw_text):
    # The basic Web plugin is a text cleaner.
    text = raw_text.lower()

    # Find entry point (start of composition)
    start_keywords = ['состав:', 'курамы:', 'ингредиенты:', 'сосiаb', 'соспав']
    start_index = -1
    for key in start_keywords:
        if key in text:
            start_index = text.find(key) + len(key)
            break

    # Take the text after the keyword (or all if not found)
    content = text[start_index:] if start_index != -1 else text

    # Regular: leave letters, numbers and commas
    cleaned = re.sub(r'[^а-яa-z0-9,\s]', '', content)

    # Comma Tagging
    raw_tokens = [t.strip() for t in cleaned.split(',')]

    return filter_ingredients(raw_tokens)


if __name__ == "__main__":
    # Test run: check the cleaning logic
    sample = "СОСТАВ: Молоко, сахар, E500. Изготовитель: ООО 'Молоко', тел: 123"
    print("Testing Processor:", clean_and_split(sample))
