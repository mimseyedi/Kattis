n = int(input())
r = list(map(int, input().split()))

h = 0

for i in r:
    if i < 0:
        h += i

print(abs(h))
