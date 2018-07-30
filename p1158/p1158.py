import sys


num_set = list(map(int, sys.stdin.readline().rstrip().split(" ")))
total_num = num_set[0]
div = num_set[1] - 1

num_list = list(range(1, total_num + 1))
_len = len(num_list)

ind = 0
answer = []
while _len:
    ind += div
    ind = ind % _len
    selected = num_list[ind]
    answer.append(str(selected))
    num_list.remove(selected)
    _len = len(num_list)

print('<' + ', '.join(list(answer))  + '>')
