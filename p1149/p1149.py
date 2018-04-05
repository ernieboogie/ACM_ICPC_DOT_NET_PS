num_home = input("")

cost_table=[]
value_table = []
for i in range(num_home):
    cost = raw_input("")
    cost_i = []
    for elem in cost.split(" "):
        cost_i.append(int(elem))
    cost_table.append(cost_i)


for i in range(num_home):
    value_i = []
    if(i == 0):
        value_i.append(cost_table[0][0])
        value_i.append(cost_table[0][1])
        value_i.append(cost_table[0][2])
    else:
        #R
        value_i.append(min(value_table[i-1][1] + cost_table[i][0], value_table[i-1][2] + cost_table[i][0]));
        #G
        value_i.append(min(value_table[i-1][0] + cost_table[i][1], value_table[i-1][2] + cost_table[i][1]));
        #B
        value_i.append(min(value_table[i-1][0] + cost_table[i][2], value_table[i-1][1] + cost_table[i][2]));
    value_table.append(value_i)

print min(value_table[i][0], value_table[i][1], value_table[i][2])
