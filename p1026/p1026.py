_length  = input("")

list1 = []
list2 = []
current = 0

def swap(l1, ind1, ind2):
    new_l = l1
    temp = new_l[ind1]
    new_l[ind1] = new_l[ind2]
    new_l[ind2] = temp
    return new_l

def calc(l1, l2, length):
    _sum = 0
    for i in range(length):
        _sum = _sum + l1[i] * l2[i]
    return _sum

for elem in raw_input("").split(" "):
    list1.append(int(elem))
for elem in raw_input("").split(" "):
    list2.append(int(elem))
list1.sort()
list2.sort(reverse = True)
print calc(list1, list2, _length)
