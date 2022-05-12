company, n = map(int, input().split())
locations = list(map(int, input().split()))
companyLocations = {c: locations[c-1] for c in range(1, company + 1)}

for _ in range(n):
    sign, a, b = map(int, input().split())
    if sign == 1:
        companyLocations[a] = b
    else:
        print(abs(companyLocations[a] - companyLocations[b]))
