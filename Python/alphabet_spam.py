text = input()

res = len(text)
whitespaces = 0
lowerCaseLetters = 0
upperCaseLetters = 0
symbols = 0

for i in text:
    if i == "_":
        whitespaces += 1
    elif i.islower():
        lowerCaseLetters += 1
    elif i.isupper():
        upperCaseLetters += 1
    else:
        symbols += 1

print(whitespaces / res)
print(lowerCaseLetters / res)
print(upperCaseLetters / res)
print(symbols / res)
