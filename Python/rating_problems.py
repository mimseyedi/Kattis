judges, pJudges = map(int, input().split())
invisPoint = judges - pJudges

maxList = list()
minList = list()
for i in range(pJudges):
    point = int(input())
    maxList.append(point)
    minList.append(point)

if invisPoint != 0:
    for j in range(invisPoint):
        maxList.append(3)
        minList.append(-3)

maxS = 0
for m in maxList:
    maxS += m

minS = 0
for m in minList:
    minS += m
    
print(f'{minS / judges} {maxS / judges}')
