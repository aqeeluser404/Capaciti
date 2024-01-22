# Floating Point Numbers (Floats)

# Float is the data type that manages numbers with decimal places with very accurate precision. 
# The float data type can be called as a function with zero or 1 argument of any data type. 
# If no argument is given, then float returns 0.0.

# Example of float function:
x = float(5)
y = float("21.765")

# String value cast to a float must contain only numbers and only one occurrence of the dot (.) character.
# Example:
# float("FF909A") will raise an exception.

# Formatting Floats
# Example:
print ("Today's Dollar price compared to the Rand: R%f" % 6.85871)
# Output: Today's Dollar price compared to the Rand: R6.858710

print ("Today's Dollar price compared to the Rand: R%.2f" % 6.85871)
# Output: Today's Dollar price compared to the Rand: R6.86

print ("Change since yesterday: R%+.2f" % 0.5)
# Output: Change since yesterday: R+0.50

# The f in the format part of the print statement indicates that the number to be formatted is a float.
# The + sign indicates that the changed amount must be signed, which means that if the dollar compared to the rand decreases, that a − sign would be printed before the amount difference.

# Examples:
print ("Negative amount: %+f" % -0.23)
# Output: Negative amount: -0.230000

print ("Positive amount: %+f" % 0.23)
# Output: Positive amount: +0.230000