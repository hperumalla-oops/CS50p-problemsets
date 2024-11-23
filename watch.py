import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if "iframe" not in s:
        return None

    p= r'(https?://www\.youtube\.com/embed/[A-Za-z0-9]{11})'
    q= r'(https?://youtube\.com/embed/[A-Za-z0-9]{11})'

    #print(re.search(p,s))
    #print(re.search(q,s))

    if bool(re.search(p,s)):
        #print("ok")
        x=re.search(p,s).group()
        return "https://youtu.be/"+ re.search(r'[A-Za-z0-9]{11}',x).group()

    elif bool(re.search(q,s)):
        x=re.search(q,s).group()
        return "https://youtu.be/"+ re.search(r'[A-Za-z0-9]{11}',x).group()

    else:
        None


if __name__ == "__main__":
    main()


