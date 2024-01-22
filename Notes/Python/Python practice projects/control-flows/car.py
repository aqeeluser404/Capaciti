#  Input in a number representing a car type, until the number 0 is input. There are three types of cars: 1 = luxury, 2 = commercial, 3 = sedan. Count how many of each type there are and print out this total with a message stating what type of car it is. 

luxury_count = 0
commercial_count = 0
sedan_count = 0

while True:
    car_type = int(input("Enter car type (1 = luxury, 2 = commercial, 3 = sedan, 0 to exit): "))

    if car_type == 0:
        break

    if car_type == 1:
        luxury_count += 1
    elif car_type == 2:
        commercial_count += 1
    elif car_type == 3:
        sedan_count += 1
    else:
        print("Invalid input. Please enter 1, 2, 3, or 0.")

print(f"Total luxury cars: {luxury_count}")
print(f"Total commercial cars: {commercial_count}")
print(f"Total sedan cars: {sedan_count}")

