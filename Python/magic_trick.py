s = input()
result = 1

for i in range(len(s)):
    j = s[i]
    for k in range(i + 1, len(s)):
        if j == s[k]:
            result = 0

print(result)
