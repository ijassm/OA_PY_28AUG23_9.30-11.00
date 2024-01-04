##print("hello", end="-")
##print("world", end="")
##print("☻")

##for i in range(1,26):
##    if(i > 9):
##        print(i, end=" ")
##    else:
##        print(" " + str(i), end =" ")
##    if(i % 5 == 0):
##        print()
    

for i in range(1,26):
    print("{:2d}".format(i), end=" ")
    if(i % 5 == 0):
        print()
