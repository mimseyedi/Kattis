s = input()
counter = 0
hey = str()

for i in s:
    if i == 'e':
        counter += 1

for i in range(counter * 2):
    hey += 'e'

print(f'h{hey}y')
