word = raw_input("").upper()

wordCount = dict()
for char in word:
    if not char in wordCount:
        wordCount[char] = 1

    else: # word is in dictionary
        wordCount[char] += 1

_max = 0
_max_char = None
for key,val in wordCount.items():

    if _max == 0:
        _max_char = key
        _max = val

    elif _max == val:
        _max_char = '?'

    elif _max < val:
        _max_char = key
        _max = val

print _max_char
