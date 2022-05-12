string = input()

for i in range(0, len(string) - 1):
    if string[i] == ':' and string[i + 1] == ')':
        print(i)
    elif string[i] == ';' and string[i + 1] == ')':
        print(i)
    elif string[i] == ';' and string[i + 1] == '-' and string[i + 2] == ')':
        print(i)
        print(i)
    elif string[i] == ':' and string[i + 1] == '-' and string[i + 2] == ')':
        print(i)
