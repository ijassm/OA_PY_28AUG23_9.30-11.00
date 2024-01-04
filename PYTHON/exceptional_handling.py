try:
    print(a)
except NameError:
    print("Please declare a variable")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("All done successfully")
finally:
    print("All done")