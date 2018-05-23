import sys
import fractions

num_of_test = int(sys.stdin.readline().rstrip())

for _ in range(num_of_test):

    num_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    A = num_list[0]
    B = num_list[1]

    gcd = fractions.gcd(A,B)

    sys.stdout.write(str(int(A * B / gcd)) + '\n')
