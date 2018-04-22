def checkGroupWord(word):
    charList = []

    for char in word:

        if not char in charList:
            charList.append(char)

        elif char in charList and charList[-1] == char:
            pass

        elif char in charList and charList[-1] != char:
            return False

    return True

numOfWord = input("")

#number of group word
nogw = 0
for ind in range(numOfWord):

    if checkGroupWord(raw_input("")):
        nogw += 1


print nogw
