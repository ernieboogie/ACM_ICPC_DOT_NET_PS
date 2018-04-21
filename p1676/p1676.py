

num = input("")


numberOfTwo = 0
numberOfFive = 0
for number in range(num):

    number += 1

    while(number % 2 == 0):
        numberOfTwo += 1
        number = number / 2

    while(number % 5 == 0):
        numberOfFive += 1
        number = number / 5


print min(numberOfTwo, numberOfFive)
