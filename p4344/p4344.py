import sys

for test in range(int(sys.stdin.readline().strip())):

    score_info =list(map(int, sys.stdin.readline().rstrip().split(" ")))
    num_of_student =score_info[0]

    total_score = sum(score_info) - num_of_student
    average = float(total_score) / float(num_of_student)

    over_student = 0
    for ind in range(1, len(score_info)):

        if average < score_info[ind]:
            over_student += 1


    result = float(over_student) / num_of_student
    result *= 100

    print( '{:0.3f}' .format(result) + '%')
