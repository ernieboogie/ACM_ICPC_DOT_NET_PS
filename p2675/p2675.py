import sys

num_of_test = int(sys.stdin.readline().rstrip())


for _ in range(num_of_test):

    word_info = sys.stdin.readline().rstrip().split(" ")
    count = int(word_info[0])

    for alpha in word_info[1]:
        sys.stdout.write(alpha * count)

    sys.stdout.write('\n')


    
