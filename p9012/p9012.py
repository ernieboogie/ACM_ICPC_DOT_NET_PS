import sys

num_test = int(sys.stdin.readline().rstrip())


while num_test:
    paren_stack = []
    test_case = sys.stdin.readline().rstrip()
    exception = False
    for paren in test_case:

        if paren == '(':
            paren_stack.append('(')
        else:
            if len(paren_stack) > 0:
                paren_stack.pop()
            else: # error
                exception = True
                break
    if exception or len(paren_stack) > 0:
        sys.stdout.write('NO\n')
    else:
        sys.stdout.write('YES\n')

    num_test = num_test - 1
