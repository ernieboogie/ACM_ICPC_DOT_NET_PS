import sys
numList = map(int, sys.stdin.readline().split(" "))
a = numList[0]
b = numList[1]
c = numList[2]

sys.stdout.write(str((a+b)%c) + '\n')
sys.stdout.write(str((a%c+b%c)%c)+ '\n')
sys.stdout.write(str((a*b)%c)+ '\n')
sys.stdout.write(str(((a%c) * (b%c))%c)+ '\n')
