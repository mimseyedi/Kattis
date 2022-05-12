n, v, h = map(int, input().split())

ls = list()
ls.append((n - v) * (n - h) * 4)
ls.append((n - v) * h * 4)
ls.append((v) * (n - h) * 4)
ls.append(v * h * 4)

print(max(ls))
