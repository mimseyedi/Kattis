L = input()
D = input()
X = int(input())

for i in range(int(L), int(D) + 1):
    lr = 0
    for l in str(i):
        lr += int(l)
    if lr == X:
        print(i)
        break
    

for i in range(int(D), int(L) - 1, -1):
    dr = 0
    for d in str(i):
        dr += int(d)
    if dr == X:
        print(i)
        break
