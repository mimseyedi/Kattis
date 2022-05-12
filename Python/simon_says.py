n = int(input())

for _ in range(n):
    pharse = input().split()
    if pharse[0] == 'Simon' and pharse[1] == 'says':
        print(*pharse[2:])
