import matplotlib.pyplot as plt

try:
    n1 = int(input("Add meg az első számot! "))
    n2 = int(input("Add meg a második számot! "))

    def pascalhsz(n1,n2):
        if n1 <= n2:
            return "Az n1 nem nagyobb, mint az n2"
        ls = [1]
        for i in range(n1):
            print(ls)
            if i+1 == n2:
                plt.plot(ls,"go")
                plt.show()
            ls.append(0)
            for j in range(len(ls)):
                if j == 0:
                    ls2=[1]
                else:
                    ls2.append(ls[j-1]+ls[j])
            ls = ls2
    pascalhsz(n1,n2)

except ValueError:
    print("Nem egész számokat adott meg")