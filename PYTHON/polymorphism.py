# Python program for demonstrating the in-built poly-morphic functions

# # len() function is used for a string
# print(len("Javatpoint"))

# # len() function is used for a list
# print(len([110, 210, 130, 321]))

# # len() function is used for a tuple
# print(len((110, 210, 130, 321)))

# # len() function is used for a set
# print(len({110, 210, 130, 321}))

# --------------------------------------------------

# here, is a simple Python function
# for demonstrating the Polymorphism


# def add(p, q, r=0):
#     return p + q + r


# # Driver code
# print(add(6, 23))
# print(add(22, 31, 544))

# ----------------------------------------------
# Polymorphism with Class Methods
# ----------------------------------------------

# class xyz():
#     def websites(self):
#         print("Javatpoint is a website out of many availabe on net.")

#     def topic(self):
#         print("Python is out of many topics about technology on Javatpoint.")

#     def type(self):
#         print("Javatpoint is an developed website.")

# class PQR():
#     def websites(self):
#         print("Pinkvilla is a website out of many availabe on net. .")

#     def topic(self):
#         print("Celebrities is out of many topics.")

#     def type(self):
#         print("pinkvilla is a developing website.")

# obj_jtp = xyz()
# obj_pvl = PQR()
# for domain in (obj_jtp, obj_pvl):
#     domain.websites()
#     domain.topic()
#     domain.type()

# ----------------------------------------------
# Polymorphism with Inheritance:
# ----------------------------------------------

# class Birds:
#     def intro1(self):
#         print("There are multiple types of birds in the world.")
#     def flight1(self):
#         print("Many of these birds can fly but some cannot.")

# class sparrow1(Birds):
#     def flight1(self):
#         print("Sparrows are the bird which can fly.")

# class ostrich1(Birds):
#     def flight1(self):
#         print("Ostriches are the birds which cannot fly.")

# obj_birds = Birds()
# obj_spr1 = sparrow1()
# obj_ost1 = ostrich1()

# obj_birds.intro1()
# obj_birds.flight1()

# obj_spr1.intro1()
# obj_spr1.flight1()

# obj_ost1.intro1()
# obj_ost1.flight1()

# ----------------------------------
# Polymorphism with a Function and Objects
# ----------------------------------

# class xyz():
#      def websites(self):
#           print("Javatpoint is a website out of many availabe on net.")

#      def topic(self):
#           print("Python is out of many topics about technology on Javatpoint.")

#      def type(self):
#           print("Javatpoint is an developed website.")

# class PQR():
#      def websites(self):
#           print("Pinkvilla is a website out of many availabe on net. .")

#      def topic(self):
#           print("Celebrities is out of many topics.")

#      def type(self):
#           print("pinkvilla is an developing website.")

# def func(obj):
#       obj.websites()
#       obj.topic()
#       obj.type()

# obj_jtp = xyz()
# obj_pvl = PQR()

# func(obj_jtp)
# func(obj_pvl)


# ----------------------------------
# method overloading
# ----------------------------------

# First product method.
# Takes two argument and print their
# product


# def product(a, b):
#     p = a * b
#     print(p)


# Second product method
# Takes three argument and print their
# product


# def product(a, b, c):
#     p = a * b * c
#     print(p)


# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
# product(4, 5, 5)

# --------------------------------------
# code

# Method 2 (Not The Most Efficient Method):


# Function to take multiple arguments
# def add(datatype, *args):

# 	# if datatype is int
# 	# initialize answer as 0
# 	if datatype == 'int':
# 		answer = 0

# 	# if datatype is str
# 	# initialize answer as ''
# 	if datatype == 'str':
# 		answer = ''

# 	# Traverse through the arguments
# 	for x in args:

# 		# This will do addition if the
# 		# arguments are int. Or concatenation
# 		# if the arguments are str
# 		answer = answer + x

# 	print(answer)


# # Integer
# add('int', 5, 6)

# # String
# add('str', 'Hi ', 'Geeks')


# Method 3 (Not The Most Efficient Method):

# def add(a=None, b=None):
# 	# Checks if both parameters are available
# 	# if statement will be executed if only one parameter is available
# 	if a != None and b == None:
# 		print(a)
# 	# else will be executed if both are available and returns addition of two
# 	else:
# 		print(a+b)


# # two arguments are passed, returns addition of two
# add(2, 3)
# # only one argument is passed, returns a
# add(2)
