numList = map(int, raw_input().split(" "))
numList.sort()
a = numList[0]
b = numList[1]

#gcd
#lcm
ab = a * b
gcd = 0
lcm = 0

while max(a,b) % min(a,b) != 0:

    if max(a,b) == a:
        a = a % b
    else:
        b = b % a


gcd = min(a,b)
lcm = ab / gcd

print gcd
print lcm
