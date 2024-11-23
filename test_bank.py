from pizza.pizza import value
def main():
    test_words()
    test_sentences()
    test_characters()
    test_capitals()


def test_words():
    assert value("hello") == 0
    assert value("wassup") == 100
    assert value("loser") == 100
    assert value("howdy") == 20

def test_sentences():
    assert value("When you use a bird to write with, it's called tweeting.") == 100
    assert value("Get lost loser!!") == 100

def test_capitals():
    assert value("HELLO") == 0
    assert value("WASSUP") == 100
    assert value("loser") == 100

def test_characters():
    assert value("w31rdalpAbets#%^") == 100
    assert value("1N73LL1G3NC3 ##weird") == 100
    assert value("hadoop#%^") == 20

if __name__ == "__main__":
    main()
