import sys

def calc_self(num):

    a = int(num / 1000)
    b = int( ( num % 1000) / 100)
    c = int((num % 100) / 10 )
    d = int(num % 10)


    return num+a+b+c+d
num_list = list(range(1,10000))
result_list = list(range(1,10000))

for num in num_list:

    calc_result = calc_self(num)

    if calc_result < 10000:
        if calc_result in result_list:
            result_list.remove(calc_result)
            #delete

for elem in result_list:
    sys.stdout.write(str(elem) + '\n')
