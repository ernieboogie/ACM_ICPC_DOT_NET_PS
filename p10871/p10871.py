import sys

numInfo = map(int, sys.stdin.readline().rstrip().split(" "))
compareNum = numInfo[1]


numList = map(int, sys.stdin.readline().rstrip().split(" "))
ansList = []
for numElem in numList:
    if compareNum > numElem:
        ansList.append(str(numElem))
sys.stdout.write(" ".join(ansList) + "\n")
