s = input()
checkHis = bool()

for i in range(len(s) - 1):
    if s[i] == 's' and s[i + 1] == 's':
        checkHis = True
        break
    else:
        checkHis = False

print('hiss' if checkHis else 'no hiss')
