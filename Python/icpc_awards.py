n = int(input())

uni = list()
team = list()
winners = list()

for _ in range(n):
    u, t = input().split()
    uni.append(u)
    team.append(t)

for i in range(len(uni)):
    if uni[i] not in winners:
        winners.extend([uni[i], team[i]])

for j in range(0, 23, 2):
    print(f'{winners[j]} {winners[j + 1]}')
