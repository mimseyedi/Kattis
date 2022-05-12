string = input()

finallStringList = list()
examStringList = list()

for i in string:
    examStringList.append(i)

for i in range(len(string) - 1):
    if string[i] not in examStringList[i + 1]:
        finallStringList.append(string[i])

finallStringList.append(examStringList[-1])
print(''.join(finallStringList))
