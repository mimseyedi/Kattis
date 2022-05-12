n = int(input())
javelins = list()

for _ in range(n):
    ja = int(input())
    javelins.append(ja)

result = 0
for j in javelins:
    result += j

result -= n - 1

print(result)
