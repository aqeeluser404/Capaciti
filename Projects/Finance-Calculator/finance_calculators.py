import math

def main():
    print("Welcome to the Finance Calculator!")
    
    while True:
        print("\nChoose an option:")
        print("1. Investment")
        print("2. Bond")
        print("3. Quit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1" or choice.lower() == "investment":
            calculate_investment()
        elif choice == "2" or choice.lower() == "bond":
            calculate_bond()
        elif choice == "3" or choice.lower() == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

def calculate_investment():
    principal = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    if rate > 100.00:
        print("\n Interest rate cannot be above 100%, enter amount that is below")

    time = int(input("Enter the number of years you plan on investing for: "))
    
    interest_type = input("Do you want 'simple' or 'compound' interest: ").lower()
    
    if interest_type == "simple":
        amount = principal * (1 + rate * time)
    elif interest_type == "compound":
        amount = principal * math.pow(1 + rate, time)
    else:
        print("Invalid interest type. Please choose 'simple' or 'compound'.")
        return
    
    print(f"Your investment will be worth: R {amount:.2f}")

def calculate_bond():
    house_value = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the annual interest rate: ")) / 12 / 100
    months = int(input("Enter the number of months for repayment: "))
    
    monthly_payment = (rate * house_value) / (1 - math.pow(1 + rate, -months))
    
    print(f"Your monthly bond repayment will be: R {monthly_payment:.2f}")


main()
