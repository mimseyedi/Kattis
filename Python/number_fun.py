n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())
    maxd = max(a, b)
    mind = min(a, b)
    if a + b == c or a * b == c or maxd - mind == c or maxd / mind == c:
        print('Possible')
    else:
        print('Impossible')
