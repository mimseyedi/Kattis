line = input().split()

pattern = [1, 1, 2, 2, 2, 8]

i = 0
result = list()

for piece in line:
    piece = int(piece)
    result.append(str(pattern[i] - piece))
    i += 1

print(' '.join(result))
