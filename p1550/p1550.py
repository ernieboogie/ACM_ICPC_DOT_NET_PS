hexMap = dict()
hexMap['0'] = 0
hexMap['1'] = 1
hexMap['2'] = 2
hexMap['3'] = 3
hexMap['4'] = 4
hexMap['5'] = 5
hexMap['6'] = 6
hexMap['7'] = 7
hexMap['8'] = 8
hexMap['9'] = 9
hexMap['A'] = 10
hexMap['B'] = 11
hexMap['C'] = 12
hexMap['D'] = 13
hexMap['E'] = 14
hexMap['F'] = 15

hexdecimal = list(raw_input())
hexdecimal.reverse()

decimal = 0


for i in range(len(hexdecimal)):

    decimal += pow(16,i) * hexMap[hexdecimal[i]]

print decimal
