n = int(input())

words = list()
for i in range(n):
    word = input()
    words.append(word)

for i in range(0, n, 2):
    print(words[i])
