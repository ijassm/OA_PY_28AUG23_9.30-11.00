import functools
# l = [1, 2, 4, 6, 8]


# def sum(l):
#     # l = [*l]
#     print(id(l))


# # sum([*l])
# sum(l)
# print(id(l))

# ---------------------------------

# l = [1, 2, 4, 6, 8]


# def double(l):
#     l = [*l]
#     result = []
#     for i in l:
#         result.append(i ** 2)
#     return result


# def triple(l):
#     l = [*l]
#     result = []
#     for i in l:
#         result.append(i ** 3)
#     return result


# def quadruple(l):
#     l = [*l]
#     result = []
#     for i in l:
#         result.append(i ** 4)
#     return result


# def quintuple(l):
#     l = [*l]
#     result = []
#     for i in l:
#         result.append(i ** 5)
#     return result


# print(double(l))
# print(triple(l))
# print(quadruple(l))
# print(quintuple(l))

def hof(logicFunc, l):
    l = [*l]
    result = []
    for i in l:
        result.append(logicFunc(i))
    return result


# def double(i):
#     return i * 2


# def triple(i):
#     return i * 3


# def quadruple(i):
#     return i * 4


# def quintuple(i):
#     return i * 5

l = [1, 2, 4, 6, 8]

d = hof(lambda i: i * 2, l)
t = hof(lambda i: i * 3, l)
qd = hof(lambda i: i * 4, l)
qt = hof(lambda i: i * 5, l)

print()

map_d = map(lambda i: i * 2, l)
filter = filter(lambda i: i > 4, l)
reduce = functools.reduce(lambda acc, element: acc + element, l)

# acc   element   acc
# 0   +   1     =  1
# 1   +   2     =  3
# 3   +   4     =  7
# 7   +   6     =  13
# 13  +   8     =  21

# = 21

# print(list(filter))
print(reduce)

# print(d)
# print(list(map_d))
# print(t)
# print(qd)
# print(qt)
