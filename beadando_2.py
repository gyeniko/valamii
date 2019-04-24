try:
    n1=int(input("Add meg az első számot! "))
    n2=int(input("Add meg a második számot! "))

    szam = 1
    for i in range(n1):
        for j in range(i+1):
            if j > 0:
                szam = szam * ((i+1)-j)/j
            print(int(szam),end=" ")
        print()

except ValueError:
    print("Nem egész számot adott meg")
