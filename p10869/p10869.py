numList = []

for nums in raw_input("").split(" "):
    numList.append(int(nums))


print numList[0] + numList[1]
print numList[0] - numList[1]
print numList[0] * numList[1]
print int(numList[0] / numList[1])
print numList[0] % numList[1]
