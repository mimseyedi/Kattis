n = input()
ls = list(map(int, input().split()))

s = 0
c = 0
for x in ls:
    if x >= 0:
        s += x
        c += 1

print(s / c)
