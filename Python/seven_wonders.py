s = input()

t = s.count('T')
c = s.count('C')
g = s.count('G')

res = (t ** 2) + (c ** 2) + (g ** 2) + (min(t, c, g) * 7)
print(res)
