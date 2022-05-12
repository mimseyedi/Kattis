g, s, c = map(int, input().split())

vicCards = {8: 'Province', 5: 'Duchy', 2: 'Estate'}
treCards = {6: 'Gold', 3: 'Silver', 0: 'Copper'}

goldPower, silverPower, copperPower = 3, 2, 1
gold, silver, copper = g * goldPower, s * silverPower, c * copperPower

money = gold + silver + copper

vKeys = list(vicCards.keys())
tKeys = list(treCards.keys())

outPut = list()

if money >= vKeys[0]: outPut.append(vicCards[8])
elif vKeys[1] <= money < vKeys[0]: outPut.append(vicCards[5])
elif vKeys[2] <= money < vKeys[1]: outPut.append(vicCards[2])

if money >= tKeys[0]: outPut.append(treCards[6])
elif tKeys[1] <= money < tKeys[0]: outPut.append(treCards[3])
elif tKeys[2] <= money < tKeys[1]: outPut.append(treCards[0])

if len(outPut) > 1:
    print(f'{outPut[0]} or {outPut[1]}')
else:
    print(*outPut)
