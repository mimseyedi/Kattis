s = input().split()

ls = dict()
for i in s:
    ls[i[0]] = 0

for i in s:
    ls[i[0]] += i.count(i[0])

print(max(ls.values()))
