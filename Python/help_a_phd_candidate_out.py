n = int(input())

for _ in range(n):
    s = input()
    if '+' in s:
        s = s.split('+')
        print(int(s[0]) + int(s[1]))
    else:
        print('skipped')
