dataSetNumber = int(input())
dataSets = dict()
finallDataSet = dict()

for _ in range(dataSetNumber):
    dataLine = input().split()
    dataSets[int(dataLine[0])] = int(dataLine[1])

for key, value in dataSets.items():
    sum = 0
    for i in range(1, value + 1):
        sum += i + 1
    
    finallDataSet[str(key)] = str(sum)

for key, value in finallDataSet.items():
    print(f'{key} {value}')
