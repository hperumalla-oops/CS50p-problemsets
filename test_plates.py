from plates import is_valid
import pytest

def main():
    test_words()
    test_sentences()
    test_lenght()
    test_new()
    test_length()


def test_words():
    assert is_valid("12") == False
    assert is_valid("22") == False


def test_sentences():
    assert is_valid("!@") == False
    assert is_valid("@1") == False
    assert is_valid("!a") == False


def test_new():
    assert is_valid("!@hel") == False
    assert is_valid("we@1") == False
    assert is_valid("sad!a") == False


def test_lenght():
    assert is_valid("AA0") == False
    assert is_valid("0B") == False

def test_length():
    assert is_valid("B") == False
    assert is_valid("A") == False

if __name__ == "__main__":
    main()
