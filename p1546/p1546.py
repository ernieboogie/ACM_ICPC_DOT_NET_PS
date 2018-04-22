num = input("")
testScore = []

for score in raw_input("").split(" "):
    testScore.append(float(score))

_max = max(testScore)
for i in range(num):
    testScore[i] = (testScore[i] / _max * 100)

avg = sum(testScore) / num
print ("%.2f" %avg)
