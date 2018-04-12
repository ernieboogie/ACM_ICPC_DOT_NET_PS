

def calc_mat(mat, row, col):
    if row > col:
        x = col
        y = row
    else:
        x = row
        y = col

    if mat[x-1][y-1] == -1:
        if y % 2 == 0:
            calc_mat(mat, x,y/2) + calc_mat(mat, x,y/2)
        else:
            calc_mat(mat, x, (y-1)/2) + calc_mat(mat, x, (y+1)/2)
    else:
        return mat[x-1][y-1]

size_input = raw_input("")
size = size_input.split(" ")

if int(size[0]) < int(size[1]):
    row = int(size[0])
    col = int(size[1])
else:
    row = int(size[1])
    col = int(size[0])

_mat = [[-1 for _x in range(col)] for _y in range(row)]

_mat[0][0] = 0



print calc_mat(_mat, row, col)
