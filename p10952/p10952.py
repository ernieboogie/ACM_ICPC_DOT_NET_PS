import sys

while True:

    numList = map(int, sys.stdin.readline().rstrip().split(" "))
    result = sum(numList)

    if result == 0:
        if numList[0] == 0:
            break
        else:
            sys.stdout.write(str(result)+'\n')
    else:
        sys.stdout.write(str(result)+'\n')
