n = 1
while n > 0:
    n = int(input())
    mixList = list()

    for _ in range(n * 2):
        mixList.append(int(input()))

    list1, list2 = mixList[0:(n*2//2)], mixList[(n*2//2):]

    list1New, list2New = sorted(list1), sorted(list2)

    d = dict()
    for i in range(len(list1New)):
        d[list1New[i]] = list2New[i]

    for j in list1:
        print(d[j])
    print('')
