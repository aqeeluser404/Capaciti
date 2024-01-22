
def dam_reserves(release):

    capacity = 1000000

    water_released = release
    water_left = capacity - release
    water_percentage = (release / capacity) * 100

    rounded_water_percentage = round(water_percentage, 1)

    print("===================REPORT===================")
    print(f"Amount of water released {water_released}L")
    print(f"Amount of water left {water_left}L")
    print(f"Percentage: {rounded_water_percentage}%")
    print("===================REPORT===================")

print("How many millilitres of water were released?")

water = float(input())
dam_reserves(water)


