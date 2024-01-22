print("Please enter your name:")
s_name = input(str())

print("Please enter your surname:")
s_surname = input(str())

print("Please enter your current age")
i_age = input(int())

s = str(i_age)

sentence = s_name + " " 
sentence += s_surname + " is currently "
sentence += s + " year(s) old" 

print(sentence)