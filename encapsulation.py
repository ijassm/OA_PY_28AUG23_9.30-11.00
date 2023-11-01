class Base:
    var = 10

    def __init__(self, name, age):
        # Protected member
        self._name = name
        # Private member
        self.__age = age
        print("Base class constructor is called")
        print("Calling private member of base class: ", self.__age)


# Creating a derived class
class Derived(Base):
    def __init__(self):
        print("Derived class constructor is called")
        # super().__init__("xyz")
        Base.__init__(self, "abc", 15)
        print("Calling protected member of base class: ", self._name)
        # print("Calling private member of base class: ", self.__age)

        # Modify the protected variable:
        self._name = "xyz"
        print("Calling modified protected member outside class: ", self._name)

    def getName(self):
        return self._name


obj1 = Derived()
obj2 = Base("abc", 15)

# print(obj2.__age)

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._name)


# print(obj1.getName())
