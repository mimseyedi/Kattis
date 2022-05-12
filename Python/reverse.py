n = int(input())

numbers = list()
i = 0
while i < n:
    number = input()
    numbers.append(number)
    i += 1

print('\n'.join(reversed(numbers)))
