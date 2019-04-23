try:
    adottszam=int(input("Adjon meg egy egész számot!"))
    ls = []
    for i in range(100):
        szam = str(i)
        forditva = szam[::-1]
        if szam == forditva:
            print(szam)


except ValueError:
    print("Nem egész számot adott meg!")