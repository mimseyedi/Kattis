dice1, dice2 = map(int, input().split())

sumCounter = dict()

for i in range(1, dice1 + 1):
    for j in range(1, dice2 + 1):
        res = i + j
        sumCounter[res] = sumCounter.get(res, 0) + 1

ls = list()
m_k, m_v = 0, 0
for k, v in sumCounter.items():
    if m_v == v:
        ls.append(k)
    elif v > m_v:
        m_k, m_v = k, v
        ls = [k]

for i in sorted(ls):
    print(i)
