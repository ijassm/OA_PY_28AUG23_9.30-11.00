# for storing collection of data
# mutable

# l = [1, 3, 4, 5, 6, 7, 2]

# l[0] = 100

# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[-1])
# print(len(l))
# print(l[::-1])

# print(l)

# a = []

# # a.append(12)
# # a.append(55)

# for i in range(1, 101):
#     a.append(i)

# print(a)

# ------------------------------------------

# l = [1, 3, 5, 6, 33, 56, 345]

# length = len(l)
# acc = 0

# for i in range(length):
#     acc += l[i]

# for i in l:
#     acc += i

# print(acc)

# ------------------------------------------

# a = []

# Adds an element at the end of the list

# a.append(22)
# a.append(45)
# a.append(6)

# # a.clear()  # Removes all the elements from the list

# copyList = a.copy()  # Returns a copy of the list
# sameRefList = a

# sameRefList[0] = 111

# # sameRefList.clear()

# print(a)
# print(sameRefList)
# print(copyList)

# print(id(a))
# print(id(copyList))
# print(id(sameRefList))

# ------------------------------------------

a = [23, 5, 3, 1, 5, 1, 2, 45, 5]

# print(a.count(1))  # Returns the number of elements with the specified value

# someMoreElement = [111, 222, 333, 444]


# # Add the elements of a list (or any iterable), to the end of the current list
# a.extend(someMoreElement)
# a.append(someMoreElement)

# print(a)

# print(a.index(5))  # Returns the index of the first element with the specified value

# a.insert(1, 12000)  # Adds an element at the specified position

# print(a)

# a.pop(0) #Removes the element at the specified position

# a.remove(5)  # Removes the first item with the specified value

# a.reverse() # Reverses the order of the list

# a.sort(reverse=True)

# print(a)

# ------------------------------------------
