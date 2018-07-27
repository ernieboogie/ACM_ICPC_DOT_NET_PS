import sys

num_line = int(sys.stdin.readline().rstrip())

stack = []

while num_line:

    cmd = sys.stdin.readline().rstrip().split(" ")
    op = cmd[0]
    if op == "push":
        stack.append(cmd[1])
    else:
        if op == "top":
            if len(stack) > 0:
                sys.stdout.write(stack[-1]+'\n')
            else:
                sys.stdout.write(str(-1)+ '\n')
        elif op == "size":
            sys.stdout.write(str(len(stack))+'\n')
        elif op == "empty":
            if len(stack) > 0 :
                sys.stdout.write(str(0)+'\n')
            else:
                sys.stdout.write(str(1)+'\n')
        elif op == "pop":
            if len(stack) > 0:
                sys.stdout.write(str(stack[-1])+'\n')
                stack.pop()
            else:
                sys.stdout.write(str(-1) + '\n')

    num_line = num_line - 1
