n = int(input())

colors = list()
for _ in range(n):
    c = input().lower()
    colors.append(c)

counter = 0

for i in colors:
    if i.count('rose') >= 1:
        counter += 1
        continue
    elif i.count('pink') >= 1:
        counter += 1
        continue

print(counter if counter > 0 else 'I must watch Star Wars with my daughter')
