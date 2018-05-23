import sys

char2int = dict()
char2int['A'] = 2
char2int['B'] = 2
char2int['C'] = 2
char2int['D'] = 3
char2int['E'] = 3
char2int['F'] = 3
char2int['G'] = 4
char2int['H'] = 4
char2int['I'] = 4
char2int['J'] = 5
char2int['K'] = 5
char2int['L'] = 5
char2int['M'] = 6
char2int['N'] = 6
char2int['O'] = 6
char2int['P'] = 7
char2int['Q'] = 7
char2int['R'] = 7
char2int['S'] = 7
char2int['T'] = 8
char2int['U'] = 8
char2int['V'] = 8
char2int['W'] = 9
char2int['X'] = 9
char2int['Y'] = 9
char2int['Z'] = 9

delay = dict()
delay[1] = 2
delay[2] = 3
delay[3] = 4
delay[4] = 5
delay[5] = 6
delay[6] = 7
delay[7] = 8
delay[8] = 9
delay[9] = 10


word = sys.stdin.readline().rstrip()
total_delay = 0
for char in word:
    total_delay += delay[char2int[char]]



sys.stdout.write(str(total_delay) + '\n')
