# import hof
# import hof as h
# from hof import hof, reduce
from hof import *

l = [2,4,5,6]

# print(h.hof(lambda a: a **2, l))

print(hof(lambda a: a **2, l))