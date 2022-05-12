ls = list()
for _ in range(5):
    ls.append(input())

res = list()
for i in range(len(ls)):
    if 'FBI' in ls[i]:
        res.append(str(i + 1))

if len(res) == 0:
    print('HE GOT AWAY!')
else:
    print(' '.join(res))
