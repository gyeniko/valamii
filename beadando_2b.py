import matplotlib.pyplot as plt

try:
    n1 = int(input("Add meg az első számot! "))
    n2 = int(input("Add meg a második számot! "))

    def pascalhsz(n1,n2):
        if n1 <= n2:
            print("A második szám nem kisebb mint az első")
            return
        ls = [1]
        s = (n1+1) * "  " + "1"
        for i in range(n1):
            print(s)
            if i+1 == n2:
                plt.plot(ls,"go")

            ls.append(0)
            for j in range(len(ls)):
                if j == 0:
                    ls2=[1]
                else:
                    ls2.append(ls[j-1]+ls[j])
            ls = ls2
            s = "  " * (n1-i)
            for x in ls:
                if x < 10:
                    s += str(x)
                    s += "   "
                elif x < 100:
                    s += str(x)
                    s += "  "
                else:
                    s += str(x)
                    s += " "
        plt.show()
    pascalhsz(n1,n2)

except ValueError:
    print("Nem egész számokat adott meg")