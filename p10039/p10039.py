import sys

result = []
for ind in range(5):
    num = int(sys.stdin.readline())
    if num < 40:
        num = 40
    result.append(num)

sys.stdout.write(str(sum(result)/5) + '\n')
