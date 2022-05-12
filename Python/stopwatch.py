n = int(input())

buttonList = list()

for _ in range(n):
    buttonList.append(int(input()))

if n % 2 != 0:
    print('still running')
else:
    syn = '+'
    Sum = 0
    for i in buttonList:
        if syn == '+':
            Sum += i
            syn = '-'
        else:
            Sum -= i
            syn = '+'

    print(abs(Sum))
