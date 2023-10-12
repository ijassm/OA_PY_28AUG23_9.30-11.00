# l = [1, 2, 4, 6, 8]


# def sum(l):
#     # l = [*l]
#     print(id(l))


# # sum([*l])
# sum(l)
# print(id(l))

# ---------------------------------

l = [1, 2, 4, 6, 8]


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

def hof(l, logicFunc):
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


d = hof(l, lambda i: i * 2)
t = hof(l, lambda i: i * 3)
qd = hof(l, lambda i: i * 4)
qt = hof(l, lambda i: i * 5)

print(d)
print(t)
print(qd)
print(qt)
