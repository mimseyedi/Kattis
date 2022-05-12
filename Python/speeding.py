n = int(input())

klm = list()
dis = list()

for i in range(n):
    k, d = input().split()
    klm.append(int(k))
    dis.append(int(d))

del klm[0]
del dis[0]

mdis = dis[0]
mklm = klm[0]

res = 0
resls = list()
if len(dis) > 1:
    for i in range(len(klm) - 1):
        res = mdis / mklm
        resls.append(res)
        mdis = dis[i + 1] - dis[i]
        mklm = klm[i + 1] - klm[i]
else:
    resls.append(mdis / mklm)

if len(dis) > 1:
    res = (dis[-1] - dis[-2]) / (klm[-1] - klm[-2])
    resls.append(res)

print(int(max(resls)))
