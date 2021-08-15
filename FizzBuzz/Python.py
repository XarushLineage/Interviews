for fzbz in range(1,101):
    if fzbz % 3 == 0 and fzbz % 5 == 0:
        print(str(fzbz)+"-fizzbuzz")
        continue
    elif fzbz % 3 == 0:
        print(str(fzbz)+"-fizz")
        continue
    elif fzbz % 5 == 0:
        print(str(fzbz)+"- buzz")
        continue
    print(fzbz)
