import sys


def print_board(b_list):
    count = 0
    for elem in b_list:

        if elem == '1':
            count += 1


    if count == 4:
        return 'E'
    elif count == 3:
        return 'A'
    elif count == 2:
        return 'B'
    elif count == 1:
        return 'C'
    else:
        return 'D'

board_list_1 = list(sys.stdin.readline().rstrip().split(" "))
board_list_2 = list(sys.stdin.readline().rstrip().split(" "))
board_list_3 = list(sys.stdin.readline().rstrip().split(" "))


print(print_board(board_list_1))
print(print_board(board_list_2))
print(print_board(board_list_3))
