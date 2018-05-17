import sys

i = 0
numOfHorse = 0
while i <= 7:

    chessLine = sys.stdin.readline().rstrip()

    ind = i % 2
    while ind <= 7:

        if chessLine[ind] == "F":
            numOfHorse += 1


        ind += 2
    i += 1

sys.stdout.write(str(numOfHorse)+"\n")
