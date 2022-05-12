ww = int(input())
n = int(input())

lst = list()
for _ in range(n):
    w, l = map(int, input().split())
    lst.append(w * l)

print(sum(lst) // ww)
