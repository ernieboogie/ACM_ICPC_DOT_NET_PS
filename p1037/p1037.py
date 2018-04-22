numOfDivisor = input("")

divisorList = []
for divisor in raw_input("").split(" "):
    divisorList.append(int(divisor))

divisorList.sort()
if numOfDivisor  == 1:

    print divisorList[0] * divisorList[0]

else:

    print divisorList[0] * divisorList[-1]
