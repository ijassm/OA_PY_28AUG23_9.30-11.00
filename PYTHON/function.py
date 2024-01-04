# def greeting(name):
#     print("hello" + " " + name)


# greeting("ocean")
# print("outside func")
# greeting("asoon")

# local and global scope

# a, b, c = 2, 2, 0


# def sum():
#     global c
#     c = a + b
#     # print(a,b,c)


# print(c)
# sum()
# print(c)

# return in func

# a = 12
# b = 9
# s1 = 0
# s2 = 0


# def sum(a, b):
#     global s1
#     s1 = a + b
#     print(s1)


# def sub(a, b):
#     global s2
#     s2 = a - b
#     print(s2)


# sum(a, b)
# sub(a, b)

# mul = s1 * s2
# print(mul)
# a = 12
# b = 9
# s1 = 0
# s2 = 0

# ------------------------------------
# a = 12
# b = 9


# def sum(a, b):
#     return a + b


# def sub(a, b):
#     return a - b


# mul = sum(a, b) * sub(a, b)
# print(mul)
# ------------------------------------

# types of arguments

# Arbitrary Arguments, *args

# def sum(*args):
#     o = 0
#     for i in args:
#         o += i
#     return o


# print(sum(2, 4))
# print(sum(5, 4, 7))
# print(sum(3, 4, 2, 8))
# print(sum(8, 4, 2, 8, 23))

# Keyword Arguments
# Default parameter

# def person(name, age, location="cuddalore"):
#     print(f"Myself {name}")
#     print(f"My age is {age}")
#     print(f"Am from {location}")


# person(age=12, name="ocean")


# Arbitrary Keyword Arguments
# **args

# d = {
#     "name": "ocean",
#     "age": 12,
#     "location": "pondy"
# }

# print(d["name"])
# print(d["age"])


# def person(**args):
#     print(f"Myself {args['name']}")
#     print(f"My age is {args['age']}")
#     print(f"Am from {args['location']}")

# person(name="ocean", age=12, location="pondy")


# recursion


def recursive(i):
    if (i != 0):
        recursive(i - 1)
        print(f"recursive {i}")


recursive(100)
