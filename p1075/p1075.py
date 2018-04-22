numA = input("")
numB = input("")

answer = 0

numA = int(numA / 100) * 100
while(answer < 100):


    if (numA + answer) % numB == 0:
        break

    answer += 1


if answer >= 10:
    print answer

else:
    print '0'+str(answer)
