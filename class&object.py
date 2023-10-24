# def person(name, age):
#     return {
#         "name": name,
#         "age": age,
#     }


# obj1 = person("ocean", 20)
# obj2 = person("xxx", 11)

# print(obj1)
# print(obj2)


class Person:
    pass


obj1 = Person()
obj2 = Person()


print(id(obj1))
print(id(obj2))

obj1.name = "abc"
obj1.age = 20

obj2.name = "xyz"
obj2.age = 15

print(obj1.name)
print(obj1.age, "\n")

print(obj2.name)
print(obj2.age)
