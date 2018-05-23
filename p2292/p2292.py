roomNum = input()

dst = 1
count = 0
while roomNum > dst:


    dst += 6 * count
    count += 1
if roomNum == 1:
    count = 1

print count
