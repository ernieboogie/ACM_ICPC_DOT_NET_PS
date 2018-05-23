import sys

croa_char = ['c=', 'c-', 'dz=' , 'd-', 'lj', 'nj', 's=', 'z=']

word = sys.stdin.readline().rstrip()
for croa in croa_char:

    while croa in word:
        word = word.replace(croa, '_')



sys.stdout.write(str(len(word)) + '\n')
