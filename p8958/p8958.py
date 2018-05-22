import sys

num_of_test = int(sys.stdin.readline().rstrip())

for test in range(num_of_test):

    test_result = sys.stdin.readline().rstrip()

    result = 0
    cascade = 0

    for res in test_result:

        if res == 'O':
            cascade += 1
            result += cascade

        else:
            cascade = 0

    sys.stdout.write(str(result)+ '\n')
