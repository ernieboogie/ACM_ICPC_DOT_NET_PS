import sys


num_max = int(sys.stdin.readline().rstrip())
numbers = list(range(1,num_max + 1))
ind = num_max
while ind:

    _input = int(sys.stdin.readline().rstrip())

    # check already pop
    if not _input in numbers:
        sys.stdout.write('NO\n')
        break

    numbers.remove(_input)
    ind = ind - 1
