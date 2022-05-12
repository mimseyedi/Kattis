n = int(input())

for i in range(n):
    inp = input().split()
    b = int(inp[0])
    p = float(inp[1])
    mid = (60 / p) * b
    taf = (60 / p)
    print(f'{mid - taf} {mid} {mid + taf}')
