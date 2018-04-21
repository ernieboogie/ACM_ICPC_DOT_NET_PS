numberOfInput = input("")
numList = []
localMax = []
for numbers in raw_input("").split(" "):
    numList.append(int(numbers))
for ind in range(numberOfInput):
    if ind == 0:
        localMax.append(numList[ind])
    else:
        localMax.append(max(numList[ind], numList[ind] + localMax[ind-1]))

print max(localMax)
