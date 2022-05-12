pharse = input().split(' ')
yesOrNo = bool()

for i in pharse:
    if pharse.count(i) > 1:
        print('no')
        yesOrNo = True
        break
    else:
        yesOrNo = False

if yesOrNo == False:
    print('yes')
