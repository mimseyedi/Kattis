n, w, h = map(int, input().split())

for _ in range(n):
    m = int(input())
    if w == h:
        res = (2 ** 0.5) * w
        if m > res:
            print('NE')
        else:
            print('DA')
    else:
        res = ((w ** 2) + (h ** 2)) ** 0.5
        if m > res:
            print('NE')
        else:
            print('DA')
