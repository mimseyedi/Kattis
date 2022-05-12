n = int(input())

for _ in range(n):
    number = int(input())
    result = 1
    for i in range(1, number + 1):
        result = result * i

    print(str(result)[-1])
