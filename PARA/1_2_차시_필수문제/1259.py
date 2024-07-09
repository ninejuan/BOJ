while True:
    pn = input()
    if pn == "0": break
    elif pn == pn[::-1]: print("yes")
    else: print("no")
