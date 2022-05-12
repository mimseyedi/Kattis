n = int(input())

for _ in range(n):
    store = int(input())
    loc = list(map(int, input().split()))
    dist = 2 * (max(loc) - min(loc))

    print(dist)
