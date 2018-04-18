
def print_hobit(HList, x, y):
    for i in range(9):
        if i == x or i == y:
            pass
        else:
            print HList[i]
def sum_height(HList, x, y):
    _sum = 0
    for i in range(9):
        if i == x or i == y:
            pass
        else:
            _sum += HList[i]
    return _sum

heightList = []
Find = False
for ind in range(9):
    heightList.append(input(""))
heightList.sort()
for first in range(9):
    for second in range(9):

        if first == second:
            pass

        else:
            if sum_height(heightList, first, second) == 100:
                print_hobit(heightList, first, second)
                Find = True
                break;
    if Find:
        break;
