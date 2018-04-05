num_stairs = input("")
cost_table = [0]
value_table = []
for i in range(num_stairs):
    cost_i = input("")
    cost_table.append(cost_i)

for i in range(num_stairs+1):
    value_i = []

    if i == 0:
        value_i.append(0)
        value_i.append(0)
    elif i == 1:
        value_i.append(cost_table[i])
        value_i.append(0)
    else:
        # 0 stack
        value_i.append(max(value_table[i-2][0],value_table[i-2][1]) + cost_table[i])
        # 1 stack
        value_i.append(value_table[i-1][0] + cost_table[i])

    value_table.append(value_i)
print max(value_table[i][0], value_table[i][1])
