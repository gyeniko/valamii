n = 100

def hanyolyanszamvan(n):
    for i in range(n):
        x = 0
        for j in str(i):
            if j in "047":
                x += 1
        if x == len(str(i)):
            print(i)

hanyolyanszamvan(n)