import sys

def find_input(num):
    # True if in stack , flase in number
    if num in stack:
        return True
    else:
        return False

num_max = int(sys.stdin.readline().rstrip())
numbers = list(range(1,num_max + 1))
stack = []
stack_top = 0
cmd = ''
ind = num_max
exception = False
while ind:
    print(numbers)
    print(stack)
    _input = int(sys.stdin.readline().rstrip())

    if find_input(_input):
        if _input > stack_top:
            #error
            exception = True
            pass
        elif _input == stack_top:
            cmd += '-'
            stack.remove(_input)
            stack_top = stack[-1]
        elif _input < stack_top:
            for elem in stack:
                if elem >= _input:
                    stack.remove(elem)
                    stack_top = stack[-1]
                    cmd += '-'

    else:
        for elem in numbers:
            print(elem)
            if elem < _input:
                stack.append(elem)
                numbers.remove(elem)
                stack_top = stack[-1]
                cmd += '+'
            elif elem == _input:
                numbers.remove(elem)
                cmd += '+-'
    ind = ind - 1

sys.stdout.write(cmd+'\n' + str(exception))
