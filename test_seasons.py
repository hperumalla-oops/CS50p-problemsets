from seasons import to_mins,to_words

def main():
    test_a()
    test_b()



def test_a():
    assert to_words("b") == "Invalid date"
    assert to_words("r") == "Invalid date"
    assert to_words("21") == "Invalid date"

def test_b():
    assert to_mins("9/") == "Invalid date"

if __name__ == "__main__":
    main():
