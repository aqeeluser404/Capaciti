class MyClass:
    def __init__(self):
        self.__private_var = 10  # Private variable using name mangling

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value

# Creating an instance of MyClass
obj = MyClass()

# Trying to access the private variable directly
# This will result in an AttributeError as the name is mangled
try:
    print(obj.__private_var)
except AttributeError as e:
    print("AttributeError:", e)

# Accessing the private variable using a getter method
print(obj.get_private_var())  # Output: 10

# Trying to modify the private variable directly
# This will not affect the actual variable as it's name-mangled
obj.__private_var = 20

# Accessing the private variable again using the getter method
# It remains unchanged despite the attempted modification
print(obj.get_private_var())  # Output: 10

# Modifying the private variable using a setter method
obj.set_private_var(30)

# Accessing the private variable again using the getter method
# It reflects the change made using the setter method
print(obj.get_private_var())  # Output: 30