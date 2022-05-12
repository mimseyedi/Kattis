h, m = map(int, input().split())

fullMin = (h * 60) + m
hour = (fullMin - 45) // 60
minu = (fullMin - 45) % 60

if hour == -1:
    hour = 23
    print(f'{hour} {minu}')
else:
    print(f'{hour} {minu}')
