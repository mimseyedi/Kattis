n = int(input())

for i in range(n):
    row, base, number = map(int, input().split())
    remains = list()

    while number > 0:
        remain = number % base
        number = number // base
        remains.append(remain)

    sumOfRemains = 0
    for i in range(len(remains)):
        remains[i] = remains[i] ** 2
        sumOfRemains += remains[i]

    print(f'{row} {sumOfRemains}')   
