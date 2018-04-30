num = input()


tier = 1
first = -1
second = -1

while num > tier:

    num = num - tier
    tier += 1

if tier % 2 == 0:  # from bottom
    first = num
    second = tier + 1 - first
else:
    second = num
    first = tier + 1 - second

print str(first)+'/'+str(second)
