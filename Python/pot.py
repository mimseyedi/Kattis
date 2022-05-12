n = int(input())

sum = 0
for _ in range(n):
    number = input()
    base = int(number[:-1])
    power = int(number[-1])
    sum += base ** power
    
print(sum)
