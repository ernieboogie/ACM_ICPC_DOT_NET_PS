testCase = input()

numList = map(int, raw_input().split(" "))

primeList = [2, 3, 5]

for i in range(6, 1000):

    sqrtNum = round( i  ** (1/2))
    isPrime = False
    for elem in numList:

        if sqrtNum % elem == 0:
            isPrime = False
            break
        elif sqrtNum % elem != 0 and sqrtNum <= elem:
            isPrime = True
            break
    if isPrime:
        primeList.append(i)

count = 0
for num in numList:
    if num in primeList:
        print num
        count += 1

print count
