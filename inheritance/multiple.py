# Parent class
class Parent1:
    i = 0

    def parent1_func(self):
        print(self.i)


# Parent class
class Parent2:
    j = 0

    def parent2_func(self):
        print(self.j)


class Child(Parent1, Parent2):
    def child_func(self):
        print("This is the child class")


obj = Child()
obj.i = 10
obj.j = 20
obj.child_func()
obj.parent1_func()
obj.parent2_func()
print(" The number in parent1 class : ", obj.i)
print(" The number in parent2 class : ", obj.j)
