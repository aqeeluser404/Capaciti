i_number = int(15)
s_number = str("12.543")
s_characters = str("five")
f_number = float(123.5675)

f = float(i_number)
print("An Integer cast as a floating point number:", f)

i = int(f_number)
print("A floating point number cast as an Integer:", i)

f = float(s_number)
print("A number string cast as a floating point number:", f)

#ValueError occurs as 'five' can't be converted to float
f = float(s_characters)
print("A number string cast as a floating point number:", f)
