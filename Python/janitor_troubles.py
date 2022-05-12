a, b, c, d = map(int, input().split())

r = (a + b + c + d) / 2
area = ((r-a) * (r-b) * (r-c) * (r-d)) ** 0.5

print(area)
