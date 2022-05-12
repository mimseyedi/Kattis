data = int(input())
month = int(input())

theList = list()
for s in range(month):
    x = int(input())
    theList.append(x)

left = 0
for i in theList:
    left += data - i

print(left + data)
