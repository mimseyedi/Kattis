r1, s = map(int, input().split())

if s > r1:
    r2 = s + (s - r1)
else:
    r2 = s - (r1 - s)

print(r2)
