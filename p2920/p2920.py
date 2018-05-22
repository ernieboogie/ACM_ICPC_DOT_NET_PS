import sys

_input = int("".join(sys.stdin.readline().rstrip().split(" ")))

if _input == 12345678:
    sys.stdout.write('ascending' + '\n')
elif _input == 87654321:
    sys.stdout.write('descending' + '\n')
else:
    sys.stdout.write('mixed' + '\n')
