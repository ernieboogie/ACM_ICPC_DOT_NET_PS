numPeople = input("")
waitList  = []
for time in raw_input("").split(" "):
    waitList.append(int(time))

waitList.sort()

totalTime = 0
for i in range(numPeople):
    totalTime += (numPeople - i ) * waitList[i]

print totalTime
