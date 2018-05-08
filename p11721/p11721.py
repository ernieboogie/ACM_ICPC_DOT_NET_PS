word = raw_input()

wordLen = len(word)
ind = 0
while ind < wordLen :

    if wordLen <= 10:
        print word[ind:]
    else:
        print word[ind:ind+10]

    ind += 10
