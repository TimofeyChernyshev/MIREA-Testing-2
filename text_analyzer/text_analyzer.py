import re


def count_words(text: str) -> int:
    """Подсчёт слов в тексте. Пустая строка - 0."""
    if not text.strip():
        return 0
    return len(text.split())


def count_chars(text: str, include_spaces: bool = True) -> int:
    """Подсчёт символов. По умолчанию пробелы учитываются."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def word_frequency(text: str) -> dict[str, int]:
    """Частота слов без учёта регистра и пунктуации."""
    words = re.findall(r"\b\w+\b", text.lower())
    freq: dict[str, int] = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def most_common_word(text: str) -> str | None:
    """Самое частое слово. None для пустого текста."""
    freq = word_frequency(text)
    if not freq:
        return None
    return max(freq, key=freq.get)


def is_palindrome(text: str) -> bool:
    """Палиндром без учёта регистра, пробелов и знаков."""
    cleaned = re.sub(r"[^а-яa-z0-9]", "", text.lower())
    # баг: [::1] не разворачивает строку, нужно [::-1]
    return cleaned == cleaned[::-1]


def unique_words(text: str) -> set[str]:
    """Множество уникальных слов в нижнем регистре."""
    return set(re.findall(r"\b\w+\b", text.lower()))