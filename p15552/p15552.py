import sys


num = int(sys.stdin.readline())

while num > 0:
    numList = map(int, sys.stdin.readline().split(" "))
    sys.stdout.write(str(sum(numList)) + '\n')
    num -= 1
