import emoji

y=input("Input: ")

if " " in y:
    try:
        a,b,c = y.split(maxsplit=2)
    except ValueError:
        a,b =  y.split(maxsplit=1)
        print("Output:",emoji.emojize((a),language = "alias"),emoji.emojize((b),language = "alias"))
    else:
        print("Output:",emoji.emojize((a),language = "alias"),emoji.emojize((b),language = "alias"),emoji.emojize((c),language = "alias"))

else:
    print("Output:",emoji.emojize((y),language="alias"))

