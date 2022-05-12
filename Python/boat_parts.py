p, d = map(int, input().split())

ls = list()
for _ in range(d):
    ls.append(input())

tools = 0
days = 0
uls = list()

for i in ls:
    if tools == p:
        break
    if i not in uls:
        uls.append(i)
        tools += 1
        days += 1
    else:
        days += 1

if tools < p:
    print('paradox avoided')
else:
    print(days)
