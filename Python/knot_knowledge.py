n = int(input())
a = input().split()
b = input().split()

for i in a:
    if i not in b:
        print(i)
