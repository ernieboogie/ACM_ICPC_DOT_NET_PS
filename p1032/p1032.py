def check_alphabet_index(string_set, index):
    alphabet = string_set[0][index]

    for elem in string_set:

        if alphabet == elem[index]:

            pass

        else:

            return '?'

    return alphabet


num_test = input("")

string_set = []

for _test in range(num_test):

    string_set.append(raw_input(""))

cmd_input = []
for _index in range(len(string_set[0])):

    cmd_input.append(check_alphabet_index(string_set, _index))


print ''.join(cmd_input)
