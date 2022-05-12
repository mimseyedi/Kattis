line = input()
a, b = line.split()
a = int(a)
b = int(b)

if a > b:
    print(f'{b} {a}')
elif a < b:
    print(f'{a} {b}')
else:
    print(f'{a} {b}')
