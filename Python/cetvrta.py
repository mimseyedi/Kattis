x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

ls = list()

if x1 == x2: ls.append(x3)
elif x1 == x3: ls.append(x2)
else: ls.append(x1)

if y1 == y2: ls.append(y3)
elif y1 == y3: ls.append(y2)
else: ls.append(y1)

print(f'{ls[0]} {ls[1]}')
