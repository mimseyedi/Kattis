dataSet = list()
for i in range(5):
    points = list(map(int, input().split()))
    dataSet.append(points)

finallPoints = list()
for data in dataSet:
    sum = 0
    for point in data:
        sum += point
    finallPoints.append(sum)

index = 0
result = max(finallPoints)
for i in range(len(finallPoints)):
    if result == finallPoints[i]:
        index = i + 1

print(index, result)
