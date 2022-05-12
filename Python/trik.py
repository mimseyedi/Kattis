moves = input()

ball = 1

for i in moves:
    if ball == 1 and i == 'A':
        ball = 2
    elif ball == 1 and i == 'C':
        ball = 3
    elif ball == 2 and i == 'A':
        ball = 1
    elif ball == 2 and i == 'B':
        ball = 3
    elif ball == 3 and i == 'C':
        ball = 1
    elif ball == 3 and i == 'B':
        ball = 2

print(ball)
