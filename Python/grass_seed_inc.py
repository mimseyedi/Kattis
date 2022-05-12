cost = float(input())
fields = int(input())

result = 0
for f in range(fields):
    x, y = map(float, input().split())
    result += x * y
        
print(result * cost)
