num = input()


binNum = []

while num != 0:

    if num % 2 == 0:

        binNum.append('0')
    else: # num % 2 == 1
        binNum.append('1')
        num -= 1

    num /= 2

answer = 0

for ind in range(len(binNum)):

    answer += (3 ** ind) * int(binNum[ind])


print answer
