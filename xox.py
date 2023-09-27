print("Welcome to XOX game\n")
xox = [["-"]*3, ["-"]*3, ["-"]*3]
game = True

# winingPatterns = [[]]

# while (game):
#     row1 = xox[0]
#     row2 = xox[1]
#     row3 = xox[2]

#     p1 = int(input("enter player1(X) number: "))
#     if (p1 >= 0 and p1 <= 3) and (row1[p1-1] == "-"):
#         xox[0][p1-1] = "X"
#     elif (p1 >= 4 and p1 <= 6) and (row2[p1-1] == "-"):
#         xox[1][p1-4] = "X"
#     elif (p1 >= 7 and p1 <= 9) and (row3[p1-1] == "-"):
#         xox[2][p1-7] = "X"
#     else:
#         print("invalid")

#     print("---------")
#     for i in xox:
#         print("|", *i, "|")
#     print("---------")

#     p2 = int(input("enter player2(O) number: "))
#     if (p2 >= 0 and p2 <= 3 and (row1[p2-1] == "-")):
#         xox[0][p2-1] = "O"
#     elif (p2 >= 4 and p2 <= 6 and (row2[p2-1] == "-")):
#         xox[1][p2-4] = "O"
#     elif (p2 >= 7 and p2 <= 9) and (row3[p2-1] == "-"):
#         xox[2][p2-7] = "O"
#     else:
#         print("invalid")

#     print("---------")
#     for i in xox:
#         print("|", *i, "|")
#     print("---------")

#     # game = False


# print(row1)
# print(row2)
# print(row3)

def greeting(name):
    print("hello " + name)


greeting("asoon")
greeting("ocean")
