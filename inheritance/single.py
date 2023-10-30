# Super/Base/Parent
class Parent:
    i = 10

    def parent_function(self):
        print("This is Parent class")


# Subclass/Derived/child
class Child(Parent):
    # i = 20

    def child_function(self):
        print("This is Child class", self.i)


obj1 = Parent()
obj2 = Child()

obj1.parent_function()
obj2.parent_function()
obj2.child_function()
