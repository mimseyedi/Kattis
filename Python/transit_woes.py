s, t, n = map(int, input().split())
dList = input().split()
bList = input().split()
cList = input().split()

Time = 0
for i in range(len(dList) - 1):
    Time += int(dList[i])

    if Time % int(cList[i]) == 0:
        wait = abs(Time - int(cList[i])) - int(cList[i])
    else:
        wait = abs(Time - int(cList[i]))

    Time += wait + int(bList[i])


Time += int(dList[-1])
print('yes' if Time <= t else 'no')
