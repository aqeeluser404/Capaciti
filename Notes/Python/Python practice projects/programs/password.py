import random
# initializing our character values
lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

# The string variable is created by concatenating all these character sets
string = lowerCase + upperCase + numbers + symbols

# The length variable specifies the desired length of the password.
length = 16 # initialize length

# random.sample function is used to randomly select length number of characters from the string
# the selected characters are joined together using the string.join method with an empty string as the separator
password = string.join(random.sample(string, length))

# password is printed
print("Your new password is: " + password)