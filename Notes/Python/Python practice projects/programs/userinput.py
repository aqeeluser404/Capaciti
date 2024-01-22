# Fresh Food Company Calculation

# Price per kg
Asparagus = 30.54
Beetroot = 1.45
Broccoli = 14.43
Garlic = 35.81
Potatoes = 2.04

# user input
print("Enter the amount of Asparagus (kg):")
aspa = float(input())

print("Enter the amount of Beetroot (kg):")
beet = float(input()) 

print("Enter the amount of Broccoli (kg):")
broc = float(input())

print("Enter the amount of Garlic (kg):")
garl = float(input())

print("Enter the amount of Potatoes (kg):")
pota = float(input())

# calculate
aspa = aspa * Asparagus
beet = beet * Beetroot
b = (((broc * Broccoli) * 20) / 100) # 20% discounted price
broc = (broc * Broccoli) - b # apply discount
garl = garl * Garlic
p = (((pota * Potatoes) * 30) / 100) # 30% discounted price
pota = (pota * Potatoes) - p # apply discount

total = aspa + beet + broc + garl + pota
print("The total the store has to pay: R", total)
