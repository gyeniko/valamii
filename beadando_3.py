try:
    adottszam=int(input("Adjon meg egy egész számot!"))
    for i in range(100000):
        szam = str(i)
        forditva = szam[::-1]
        if szam == forditva and i % adottszam == 0:
            print(szam)


except ValueError:
    print("Nem egész számot adott meg!")