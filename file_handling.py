# f = open("myfile.txt", "x")


# f = open("demofile.txt", "a")

# f.write("Now the file has more content!")
# f.close()


f = open("demofile.txt", "w")

f.write("Now the file has more content!")
f.close()


f = open("demofile.txt", "rt")

print(f.read())

# print(f.read(10))

# print(f.readline())
# print(f.readline())
# print(f.readline())

f.close()