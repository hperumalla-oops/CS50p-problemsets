from fuel import convert,gauge
import pytest


def main():
    test_gauge()
    test_convert()

def test_convert():
    assert convert("1/3") == 33
    with pytest.raises(ValueError):
        assert convert("meh/bhel")
    with pytest.raises(ValueError):
        assert convert("31/2")
    with pytest.raises(ZeroDivisionError):
            assert convert("7/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(35) == "35%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


if __name__ == "__main__":
    main()