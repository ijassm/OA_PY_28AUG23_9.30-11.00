user = input("enter your username :").lower()


ouser = "ocean"
opass = "12345"

##if(user == ouser and ps == opass):
##    print("successfully logged in")
##else:
##    print("invalid credential try again")

##if(False):
##    print("if 1 is working")
##if(True):
##    print("if 2 is working")
##else:
##    print("else")

##age = 101

##if(age >= 18 and age <= 100):
##    print("eligible for voting")
##elif(age <= 0):
##    print("invalid")
##elif(age > 100):
##    print("this age is not preferable for voting")
##else:
##    print("not eligible for voting")

##Nested if

if(user == ouser):
    print(f"Hi {user.upper()} you can enter your password")
    ps = input("enter your password :")
    if(ps == opass):
        print(f"{user.upper()} logged in successfully")
    else:
        print("invalid password please try one more time")
        ps = input("enter your password :")
        if(ps == opass):
            print(f"{user.upper()} logged in successfully")
        else:
            print("sorry you can't login try again later")
else:
    print("invalid credential try again")

    



