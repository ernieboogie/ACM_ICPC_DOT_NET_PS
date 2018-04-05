_height = input("")
tri_table = []
for i in range(_height):
    _input = raw_input("").split(" ")
    tri_i = []
    for elem in _input:
        tri_i.append(int(elem))
    tri_table.append(tri_i)

for i in range(_height):
    i = _height - i - 1
    if(i == 0):
        print tri_table[0][0]
        break
    for j in range(i):
        tri_table[i-1][j] = tri_table[i-1][j] + max(tri_table[i][j],tri_table[i][j+1])
