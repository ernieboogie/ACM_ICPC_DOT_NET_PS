def calculateCycle(num):

    ten = int( num / 10)
    base = num % 10

    return  base * 10 + (ten + base) % 10

num = input("")

cycle = 0
cycleNum = -1
prevCycleNum = num

while(cycleNum != num):
    cycleNum = calculateCycle(prevCycleNum)
    prevCycleNum = cycleNum
    cycle += 1



print cycle
