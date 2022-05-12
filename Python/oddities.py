n = int(input())

ls = list()
for _ in range(n):
    ls.append(int(input()))

for i in ls:
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')
