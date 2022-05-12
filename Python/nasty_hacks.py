n = int(input())

for _ in range(n):
    data = input().split()
    ewoa = int(data[0])
    ewa = int(data[1])
    coa = int(data[2])

    pwa = ewa - coa
    pwoa = ewoa 

    if pwoa < pwa:
        print('advertise')
    elif pwoa == pwa:
        print('does not matter')
    else:
        print('do not advertise')
