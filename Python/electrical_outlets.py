n = int(input())

i = 0
while i < n:
    items = input().split()
    k = int(items[0])
    sl = items[1:]
    
    result = 0
    
    for s in sl:
        result += int(s) - 1

    i += 1

    print(result + 1)
