def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(x):
    special = [
        "~",
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "-",
        "_",
        "+",
        "=",
        " ",
    ]
    r = [*x]

    for d in range(len(r)):
        if r[d] in special:
            return False  # "character present"
        else:
            d = d + 1
    else:
        if len(r) > 6 or len(r) < 2:
            return False  # "length"
        else:
            for n in range(len(r) - 1):
                try:
                    r[n] == int(r[n])
                    break
                except ValueError:
                    n = n + 1

            if n == (len(r) - 1):
                # print(0)
                return True


        if int(r[n]) == 0:
            return False  # "1st number zero"

        else:
            new = n + 1

        for new in range(n + 1, len(r)):
            # print(r[new])
            try:
                r[new] == int(r[new])
            except ValueError:
                return False  # "middle number"
            else:
                new = new + 1

        else:
            return True


if __name__ == "__main__":
    main()
