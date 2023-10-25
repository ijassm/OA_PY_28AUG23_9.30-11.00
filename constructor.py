class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.school = "imaculate"

    def getDetails(self):
        print("-----Details-----")
        print(self.name)
        print(self.age)
        print(self.school)
        print("----Details End-----")


obj1 = Person("ocean", 15)
obj2 = Person("xyz", 10)

print(obj1)
obj1.getDetails()
obj2.getDetails()
