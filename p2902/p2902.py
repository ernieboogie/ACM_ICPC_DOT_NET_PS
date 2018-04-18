
separateName = raw_input("").split("-")

reducedName = []
for elem in separateName:
    reducedName.append(elem[0])


print "".join(reducedName)
