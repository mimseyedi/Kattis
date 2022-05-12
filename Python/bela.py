n, hokm = input().split()

pointBoard = list()
for _ in range(int(n) * 4):
    point = input()
    pointBoard.append(point)

result = 0

pointDict = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'jba': 20, 
            'T': 10, '9': 0, '9ba': 14, '8': 0, '7': 0}

keys = pointDict.keys()

for k in pointBoard:
    if k[0] in keys and k[1] != hokm:
        result += pointDict[k[0]]
    elif k[0] in keys and k[1] == hokm and k[0] != 'J' and k[0] != '9':
        result += pointDict[k[0]]
    elif k[0] == 'J' and k[1] == hokm:
        result += pointDict['jba']
    elif k[0] == '9' and k[1] == hokm:
        result += pointDict['9ba']

print(result)
