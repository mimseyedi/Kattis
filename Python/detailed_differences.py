n = int(input())


for _ in range(n):
    result = list()
    r1 = input()
    r2 = input()

    for i in range(len(r1)):
        if r1[i] == r2[i]:
            result.append('.')
        else:
            result.append('*')

    print(r1)
    print(r2)
    print(''.join(result))
    print('')
