n = int(input())

l1 = list()
l2 = list()
for _ in range(n):
    t, v = input().split()
    l1.append(int(t))
    l2.append(float(v))

result = 0
for i in range(len(l1) - 1):
    result += ((l2[i] + l2[i + 1]) / 2) * (l1[i + 1] - l1[i])

print(result / 1000)
