
monthInfo = dict()

monthInfo['1'] = 31
monthInfo['2'] = 28
monthInfo['3'] = 31
monthInfo['4'] = 30
monthInfo['5'] = 31
monthInfo['6'] = 30
monthInfo['7'] = 31
monthInfo['8'] = 31
monthInfo['9'] = 30
monthInfo['10'] = 31
monthInfo['11'] = 30
monthInfo['12'] = 31

days = ["SUN","MON","TUE", "WED", "THU", "FRI", "SAT",]


numbers = map(int, raw_input().split(" "))
_sum = 0
pastMonth = 1

while(pastMonth < numbers[0]):
    _sum += monthInfo[str(pastMonth)]
    pastMonth += 1

_sum += numbers[1]


print days[_sum % 7]
