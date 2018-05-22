import sys

prob =  sys.stdin.readline().split(" ")

a = list(prob[0])
a.reverse()

b = list(prob[1])
b.reverse()

a = int("".join(a))
b = int("".join(b))

if a > b:
    sys.stdout.write(str(a) + '\n')
else:
    sys.stdout.write(str(b) + '\n')
