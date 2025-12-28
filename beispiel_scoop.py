"""  x = 1


def my_function():
    x = 10
    print("In my_function, x= " + str(x))


def my_nested_function():
    x = 100
    print("In my_nested_function, x= " + str(x))


my_nested_function()

my_function()
print("Outside of functions , x= " + str(x))

"""

try:
    int("abc")
except ValueError:
    print("Fehler")
else:
    print("OK")
