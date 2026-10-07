import pytest
from text_analyzer.text_analyzer import (
    count_words,
    count_chars,
    word_frequency,
    most_common_word,
    is_palindrome,
    unique_words,
)


class TestCountWords:
    def test_empty_string(self):
        assert count_words("") == 0

    def test_only_spaces(self):
        assert count_words("   ") == 0

    def test_single_word(self):
        assert count_words("hello") == 1

    def test_multiple_words(self):
        assert count_words("hello world") == 2
        assert count_words("one two three four") == 4


class TestCountChars:
    def test_with_spaces(self):
        assert count_chars("hello world") == 11

    def test_without_spaces(self):
        assert count_chars("hello world", include_spaces=False) == 10

    def test_empty(self):
        assert count_chars("") == 0


class TestWordFrequency:
    def test_basic(self):
        freq = word_frequency("The cat and the dog and the bird")
        assert freq["the"] == 3
        assert freq["and"] == 2
        assert freq["cat"] == 1

    def test_case_insensitive(self):
        freq = word_frequency("Hello HELLO hello")
        assert freq["hello"] == 3

    def test_empty(self):
        assert word_frequency("") == {}


class TestMostCommonWord:
    def test_basic(self):
        assert most_common_word("a a a b b c") == "a"

    def test_empty(self):
        assert most_common_word("") is None

    def test_tie(self):
        # при равенстве max вернёт первый по порядку словаря
        result = most_common_word("a b")
        assert result in {"a", "b"}


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_simple_non_palindrome(self):
        assert is_palindrome("hello") is False

    def test_with_punctuation(self):
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_russian_palindrome(self):
        assert is_palindrome("А роза упала на лапу Азора") is True

    def test_russian_non_palindrome(self):
        assert is_palindrome("привет") is False

    def test_empty(self):
        assert is_palindrome("") is True


class TestUniqueWords:
    def test_basic(self):
        assert unique_words("a b a c b") == {"a", "b", "c"}

    def test_case(self):
        assert unique_words("Hello hello HELLO") == {"hello"}

    def test_empty(self):
        assert unique_words("") == set()