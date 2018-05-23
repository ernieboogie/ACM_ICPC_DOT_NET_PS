import sys
import fractions

num_of_test = int(sys.stdin.readline().rstrip())


for _ in range(num_of_test):

    mnxy = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    M = mnxy[0]
    N = mnxy[1]
    x = mnxy[2]
    y = mnxy[3]


    if M < x or y > N :
        sys.stdout.write("-1\n")

    else:
        gcd = fractions.gcd(M,N)
        gcm = M * N / gcd


        while x != y:
            if x > gcm or y > gcm:
                break
            if x < y:
                x += M
            else:
                y += N


        if x == y and x < gcm and y < gcm:
            sys.stdout.write(str(x) + '\n')
        else:
            sys.stdout.write("-1\n")
