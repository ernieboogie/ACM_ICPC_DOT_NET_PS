import sys

def gen_num(num):
    calc = num
    for _num in list(str(num)):
        calc += int(_num)
    return calc

target_num = int(sys.stdin.readline().rstrip())
cov = 60

start_num = 1
if target_num > 60:
    start_num = target_num-60

is_set = False
answer = 0
for num in range(start_num, target_num):
    if gen_num(num) == target_num:
        is_set = True
        if answer == 0:
            answer = num

print(answer)
