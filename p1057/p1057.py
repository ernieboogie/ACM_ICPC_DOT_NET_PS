def refreshNum(player):
    newNum = 0

    if player % 2 == 0:
        newNum = player / 2
    else:
        newNum = (player + 1) / 2

    return newNum

tournamentInfo = map(int, raw_input("").split(" "))

total = tournamentInfo[0]

if tournamentInfo[1] < tournamentInfo[2]:
    playerA = tournamentInfo[1]
    playerB = tournamentInfo[2]
else:
    playerA = tournamentInfo[2]
    playerB = tournamentInfo[1]

_round = 1
while playerB - playerA != 1 or playerB % 2 != 0:

    playerA = refreshNum(playerA)
    playerB = refreshNum(playerB)

    _round += 1


print _round
