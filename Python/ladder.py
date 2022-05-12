import math

h , v = map(int, input(). split())
r = math.radians(v)
length = h / math.sin(r)
print(int(length) + 1)
