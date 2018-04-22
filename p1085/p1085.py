position = []


for elem in raw_input("").split(" "):
    position.append(int(elem))


print min(position[0], position[1], position[2] - position[0], position[3] - position[1])
