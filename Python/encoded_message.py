n = int(input())

for i in range(n):
    ls = list()
    code = input()
    cubeRowAndCol = len(code) ** 0.5

    c = int(cubeRowAndCol)

    lastC = 0
    for i in code:
        if c > len(code):
            break
        ls.append([code[lastC:c]])
        lastC += int(cubeRowAndCol)
        c += int(cubeRowAndCol)

    res = list()
    for i in range(len(ls)):
        res.append(ls[i][-1])

    result = list()

    for i in res:
        for j in i:
            result.append(j)

    k = int(cubeRowAndCol) - 1
    finall = list()

    for j in range(int(cubeRowAndCol), 0, -1):
        k = j
        for i in range(int(cubeRowAndCol)):
            finall.append(result[k - 1])
            k += int(cubeRowAndCol)

    print(''.join(finall))
