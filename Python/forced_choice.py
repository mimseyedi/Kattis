n, p, s = map(int, input().split())

sets = list()
for _ in range(s):
    sets.append(input().split()[1:])

for s in sets:
    if str(p) in s:
        print('KEEP')
    else:
        print('REMOVE')
