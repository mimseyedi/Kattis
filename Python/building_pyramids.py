n = int(input())
counter = 1

i = 0
while n >= 0:
    n -= counter ** 2
    counter += 2
    i += 1

print(i - 1)
