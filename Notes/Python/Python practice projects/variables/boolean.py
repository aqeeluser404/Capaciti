# Booleans

# Boolean data type has corresponding integer values. There are only two possible values that a Boolean variable can have, True (1) or False (0). 

# When returning Booleans as strings they are seen as “True” and “False”, and never as “1” and “0”. True and False are case-sensitive in Python.

# Boolean tests whether conditions are valid or not. The three logical operators used to test conditions between two arguments are:

# The and-operator
# The or operator
# The not operator
# The next section will refresh your memory, and you will soon be able to write programs that execute operations automatically based on decisions (such as the if statement explained in week 2). 

# The following variable values are considered False:

# False
# None
# Zero for any numeric data type, 0, 0.0, 0j
# An empty sequence or mapping. Like a list or tuple, ' ', ( ), [ ], { } 
# Instances of user-defined classes, where a class that defines a __bool__() method returns zero or False.
# All values returned otherwise are always considered true. This means that many objects will always return true.

# Operators and built-in functions that have a Boolean result always return (False or 0) or (True or 1). The Boolean or and and operations always return only one of the options, either True or False.

# Manipulate Booleans

# Syntax Description
# a or b If either a or b is True, then the result will be True. If both a and b are False then the result will be False.
# a and b If a and b are True, then the result will be True. Otherwise, the result will be False.
# not a If a is True, False is returned. If a is False, True is returned.

# Electronic diodes work on the following concept:

# Diodes can be in two states. The one state is on, and the other is off. This also means True and False respectively. Diodes have two inputs to verify what the output should be. 

# The AND gate: Both inputs have to be on in order for the gate to have an on output.

# NOT: Converts True to False, and False to True.

# Write a program that will fill in the following truth table for the example that follows:

# Dlitem Image

# Example 2: AND gate:

x = bool()
y = bool()

print ('Enter x as 1 or 0:')
x = int(input())

print ('Enter y as 1 or 0:')
y = int(input())

z = str(not bool(x and y))

print ('The Boolean value of x is', str(bool(x)))
print ('The Boolean value of y is', str(bool(y)))
print ('The Boolean value of (x and y) is', str(bool(x and y)))
print ('The Boolean value of (x not y) is', z)