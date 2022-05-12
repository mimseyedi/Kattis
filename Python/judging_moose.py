line = input()
a, b = line.split()
a = int(a)
b = int(b)

maxi = max(a, b)

if a <= 0 and b <= 0:
    print('Not a moose')
elif a == b:
    print(f'Even {a + b}')
elif a != b:
    print(f'Odd {maxi + maxi}')
