from twttr import shorten
def main():
    test_all_caps_words()
    test_sentences()
    test_characters()


def test_all_caps_words():
    assert shorten("FANTASTIC") == "FNTSTC"
    assert shorten("OMNIBUS") == "MNBS"



def test_sentences():
    assert shorten("When you use a bird to write with, it's called tweeting.") == "Whn y s  brd t wrt wth, t's clld twtng."
    assert shorten("I solemnly swear that I am upto no good") == " slmnly swr tht  m pt n gd"

def test_characters():
    assert shorten("w31rdalpAbets#$%^") == "w31rdlpbts#$%^"
    assert shorten("1N73LL1G3NC3 ##$$weird") == "1N73LL1G3NC3 ##$$wrd"



if __name__ == "__main__":
    main()