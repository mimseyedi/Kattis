d, m = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']

sumOfMonths = 0
for i in range(m - 1):
    sumOfMonths += month[i]

result = sumOfMonths + d - 1
print(days[result % 7])
