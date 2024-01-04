xox = [["-"] * 3, ["-"] * 3, ["-"] * 3]
print(xox)
game = True


def checkSameValue(l):
    value = l[0]
    if l[1] == value and l[2] == value:
        return value
    else:
        return False


def checkGame():
    global game
    isDraw = False
    r1 = xox[0]
    r2 = xox[1]
    r3 = xox[2]
    winingPatterns = [
        [r1[0], r1[1], r1[2]],
        [r2[0], r2[1], r2[2]],
        [r3[0], r3[1], r3[2]],
        [r1[0], r2[0], r3[0]],
        [r1[1], r2[1], r3[1]],
        [r1[2], r2[2], r3[2]],
        [r1[0], r2[1], r3[2]],
        [r1[2], r2[1], r3[0]],
    ]

    for i in winingPatterns:
        if checkSameValue(i) == "X":
            game = False
            return "X is winner"
        elif checkSameValue(i) == "O":
            game = False
            return "O is winner"

    for i in xox:
        if "-" not in i:
            isDraw = True
        else:
            isDraw = False

    if isDraw:
        game = False
        return "Game is Draw"


def showDisplay():
    print("---------")
    for i in xox:
        print("|", *i, "|")
    print("---------")


def updateGame(player):
    r1 = xox[0]
    r2 = xox[1]
    r3 = xox[2]
    while True:
        num = int(input(f"enter player {player} number: "))
        if (num > 0 and num <= 3) and (r1[num - 1] == "-"):
            xox[0][num - 1] = player
            break
        elif (num >= 4 and num <= 6) and (r2[num - 4] == "-"):
            xox[1][num - 4] = player
            break
        elif (num >= 7 and num <= 9) and (r3[num - 7] == "-"):
            xox[2][num - 7] = player
            break
        else:
            continue


print("Welcome to XOX game\n")
showDisplay()

while game:
    updateGame("X")
    showDisplay()
    c = checkGame()
    if c != None:
        print(c)
        break

    updateGame("O")
    showDisplay()
    c = checkGame()
    if c != None:
        print(c)
        break
