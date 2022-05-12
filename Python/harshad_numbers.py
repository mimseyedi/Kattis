n = input()

s = 0
for i in n:
    s += int(i)

if int(n) % s == 0:
    print(n)
else:
    intN = int(n)
    while intN % s != 0:
        s = 0
        intN += 1
        for j in str(intN):
            s += int(j)

    print(intN)
