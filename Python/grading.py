a, b, c, d, e = map(int, input().split())
score = int(input())

if 100 >= score >= a:
    print('A')
elif a > score >= b:
    print('B')
elif b > score >= c:
    print('C')
elif c > score >= d:
    print('D')
elif d > score >= e:
    print('E')
else:
    print('F')
