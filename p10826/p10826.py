import sys
number = int(sys.stdin.readline())

fibList = []
ind = 0

while ind <= number:
    if ind == 0:
        fibList.append(0)
    elif ind == 1:
        fibList.append(1)
    else:
        fibList.append( fibList[ind-1] + fibList[ind-2])

    ind += 1

sys.stdout.write(str(fibList[number])+'\n')
