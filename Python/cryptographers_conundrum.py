cipher = input().lower()

counter = 0
for i in range(0, len(cipher) - 2, 3):
    if cipher[i] != 'p': counter += 1
    if cipher[i + 1] != 'e': counter += 1
    if cipher[i + 2] != 'r': counter += 1

print(counter)
