n = int(input())

numbers = list()
for i in range(n):
    p, q = input().split()
    numbers.append(float(p))
    numbers.append(float(q))

s = 0
for i in range(0, len(numbers), 2):
    z = numbers[i] * numbers[i + 1]
    s += z

print(s)
