inp = input().split(';')
counter = 0

for i in range(len(inp)):
    if '-' in inp[i]:
        start, end = inp[i].split('-')
        for j in range(int(start), int(end) + 1):
            counter += 1
    else:
        counter += 1

print(counter)
