n1 = 5
ls = [1]
for i in range(n1):
    print(ls)
    ls.append(0)
    for j in range(len(ls)):
        if j == 0:
            ls2=[1]
        else:
            ls2.append(ls[j-1]+ls[j])
    ls = ls2