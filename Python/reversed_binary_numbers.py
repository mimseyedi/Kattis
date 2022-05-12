n = int(input())
binN = str(bin(n)).replace('0b', '')[::-1]
binN = '0b' + binN
print(int(binN, 2))
