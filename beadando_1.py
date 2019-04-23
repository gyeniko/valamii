n = 100

def hanyolyanszamvan(n):
    db = 0
    for i in range(n):
        x = 0
        for j in str(i):
            if j in "047":
                x += 1
        if x == len(str(i)):
            print(i)
            db += 1
    return db


print(hanyolyanszamvan(n))