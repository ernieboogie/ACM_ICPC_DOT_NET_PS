import fractions
import sys


num_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
A = num_list[0]
B = num_list[1]

gcd = fractions.gcd(A,B)

result = []
for _ in range(gcd):
    result.append('1')

sys.stdout.write("".join(result)+ '\n')
