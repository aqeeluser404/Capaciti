
def calc_bottles(litres):
    milliliters = litres * 1000 # convert to litres
    bottles = milliliters / 500 # Get bottles

    remainder = milliliters % 500 # Get remainder
    left_remainder = remainder / 500 # Get litres

    rounded_left_remainder = round(left_remainder, 2) # round 
    rounded_litres = round(litres, 2) # round 

    print(f"{rounded_litres}L water will fill {int(bottles)} 500ml bottles ({rounded_left_remainder}L remains)")

print("Enter number of litres:")
litres = float(input())
calc_bottles(litres)
