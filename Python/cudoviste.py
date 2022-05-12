row, col = map(int, input().split())

cityMap = str()
for _ in range(row):
    cel = input()
    cityMap += cel

zeroC, oneC, twoC, threeC, fourC = 0, 0, 0, 0, 0

pattern = list()
for i in range(len(cityMap) - col - 1):
    pattern.append([cityMap[i], cityMap[i+1], cityMap[i+col], cityMap[i+1+col]])

for i in range(1, row - 1):
    del pattern[i * col - i]

for pat in pattern:
    if pat.count('.') == 4:
        zeroC += 1
    elif pat.count('.') == 3 and pat.count('X') == 1:
        oneC += 1
    elif pat.count('.') == 2 and pat.count('X') == 2:
        twoC += 1
    elif pat.count('.') == 1 and pat.count('X') == 3:
        threeC += 1
    elif pat.count('X') == 4:
        fourC += 1
    
print(f'{zeroC}\n{oneC}\n{twoC}\n{threeC}\n{fourC}')
