n = int(input())

for _ in range(n):
    case = int(input())
    cities = list()
    for c in range(case):
        city = input()
        cities.append(city)

    finallCities = list()
    for c in cities:
        if c not in finallCities:
            finallCities.append(c)

    print(len(finallCities))
