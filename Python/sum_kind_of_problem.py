n = int(input())

for i in range(n):
    row, number = map(int, input().split())
    intSum, intOdd, intEven = 0, 0, 0
    intCounter, oddCounter, evenCounter = 1, 1, 2
    while intCounter <= number:
        intSum += intCounter
        intOdd += oddCounter
        intEven += evenCounter
        oddCounter += 2
        evenCounter += 2
        intCounter += 1

    print(f'{row} {intSum} {intOdd} {intEven}')
