n = int(input())
line = input().split()

counter = 0
for i in line:
    i = int(i)
    if i < 0:
        counter += 1

print(counter)
