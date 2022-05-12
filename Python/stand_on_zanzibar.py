n = int(input())

for i in range(n):
    karan = 0
    j = 0
    ls = list(map(int, input().split()))
    
    for x in range(len(ls) - 1):
        if abs(ls[x] - ls[x + 1]) > ls[x]:
            karan += ls[x + 1] - ls[x] * 2

    print(karan)
