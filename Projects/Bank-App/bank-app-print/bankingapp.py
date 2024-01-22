import math

# Welcome message for the banking app
def welcome():
    print()
    print("Welcome to the Banking App")
    print("**************************")

# Function to create a new account
def create_account():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    balance = 0
    with open("user_info.txt", "w") as file:
        file.write(f"{username} {password} {balance}")
    return username, password, balance

# Function to log into an existing account
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("user_info.txt", "r") as file:
        for line in file:
            user, pwd, balance = line.split()
            if user == username and pwd == password:
                return username, password, float(balance)
    print("User not found. Please create an account.")
    return None, None, None

# Function to handle deposit operations
def make_deposit(username, password, balance):
    while True:
        try:
            print()
            print(f"Current balance: R{balance:.2f}")
            print("************************")
            print()
            deposit = float(input("Enter the amount you want to deposit: "))
            balance += deposit
            with open("user_info.txt", "w") as file:
                file.write(f"{username} {password} {balance}")
            with open("transaction_log.txt", "a") as file:
                file.write(f"Deposit of {deposit} made. New balance: {balance}\n")
            print()
            print(f"Successfully deposited R{deposit:.2f}. New balance: R{balance:.2f}")
            print()
            break
        except ValueError:
            print("Please enter a valid number.")
    return balance

# Function to handle withdrawal operations
def make_withdrawal(username, password, balance):
    if balance <= 0:
        print("Insufficient funds. Please make a deposit.")
        return balance
    while True:
        try:
            print()
            print(f"Current balance: R{balance:.2f}")
            print("************************")
            print()
            withdrawal = float(input("Enter the amount you want to withdraw: "))
            if withdrawal <= balance:
                balance -= withdrawal
                with open("user_info.txt", "w") as file:
                    file.write(f"{username} {password} {balance}")
                with open("transaction_log.txt", "a") as file:
                    file.write(f"Withdrawal of {withdrawal} made. New balance: {balance}\n")
                print()
                print(f"Successfully withdrawn R{withdrawal:.2f}. New balance: R{balance:.2f}")
                print()
                break
            else:
                print(f"Please withdraw an amount lower than the current balance R{balance:.2f}")
        except ValueError:
            print("Please enter a valid number.")
    return balance

# Main execution of the program
if __name__ == '__main__':
    while True:
        # Display the welcome message and ask for account creation, login, or quit
        welcome()
        print()
        choice = input("Select an option: \n1. Create an account\n2. Login\n3. Quit\n\nEnter the number of your choice: ")
        print()
        if choice == "1":
            username, password, balance = create_account()
        elif choice == "2":
            username, password, balance = login()
            if username is None:
                continue
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        # Display the current balance
        print()
        print(f"Current balance: R{balance:.2f}")
        print("***********************")

        # Offer options based on balance status
        while True:
            print()
            print("Select an operation:")
            print("1. Make a deposit")
            if balance > 0:
                print("2. Make a withdrawal")
            print()
            operation_choice = input("Enter the number of your choice: ")
            if operation_choice == "1":
                balance = make_deposit(username, password, balance)
            elif operation_choice == "2" and balance > 0:
                balance = make_withdrawal(username, password, balance)
            else:
                print("Invalid choice. Please try again.")
                continue

            # Ask the user if they want to continue the banking operations
            while True:
                continue_option = input("Do you want to continue? \n1. Yes\n2. No\n\nEnter the number of your choice: ")
                if continue_option in ["1", "2"]:
                    break
                else:
                    print("Invalid choice. Please enter 1 for Yes or 2 for No.")
            if continue_option == "2":
                break
