import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Codex Bank App")

# Create frames for each screen
login_frame = tk.Frame(root, bg="#f0f0f0")
signup_frame = tk.Frame(root, bg="#f0f0f0")
bank_frame = tk.Frame(root, bg="#f0f0f0")

# global variable
balance = 0

# raise a frame to the top
def raise_frame(frame):
    frame.tkraise()

username = ''

# Login Functionality
def login():
    global username
    global balance  
    username = username_entry.get()
    password = password_entry.get()

    # Check if user exists in user_info.txt
    with open('user_info.txt', 'r') as file:
        users = file.readlines()
        for user in users:
            user_info = user.split(',')
            if user_info[0] == username and user_info[1].strip() == password:
                if len(user_info) > 2:  # Check if balance exists
                    balance = int(user_info[2])  # Update balance from user_info.txt
                    username_entry.delete(0, tk.END)
                    password_entry.delete(0, tk.END)
                else:
                    balance = 0 
                balance_label.config(text=f"Balance: R{balance}")  
                raise_frame(bank_frame)
                messagebox.showinfo("Success", "Your successfully signed in")
                return

    messagebox.showerror("Error", "Invalid username or password")
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)



# Function to handle signup
def signup():
    username = new_username_entry.get()
    password = new_password_entry.get()

    # Save new user to user_info.txt
    with open('user_info.txt', 'a') as file:
        file.write(f"{username},{password},0\n")  
        new_username_entry.delete(0, tk.END)
        new_password_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Your successfully created an account")
    raise_frame(login_frame)



def go_back_to_login():
    raise_frame(login_frame)



# Function to handle forgot password
def forgot_password():
    raise_frame(reset_password_frame)



# Function to handle password reset
def reset_password():
    username = reset_username_entry.get()
    new_password = reset_password_entry.get()

    # Check if user exists in user_info.txt
    with open('user_info.txt', 'r') as file:
        users = file.readlines()
    with open('user_info.txt', 'w') as file:
        for user in users:
            user_info = user.split(',')
            if user_info[0] == username:
                file.write(f"{username},{new_password}\n")
            else:
                file.write(user)

    messagebox.showinfo("Success", "Your password has been reset")
    raise_frame(login_frame)



# Function to handle deposit
def deposit():
    global username
    global balance 
    amount = int(deposit_entry.get())
    if amount < 0:
        messagebox.showerror("Error", "Invalid deposit amount")
        deposit_entry.delete(0, tk.END)
    else:
        balance += amount
        balance_label.config(text=f"Balance: R{balance}") 
        with open('transaction_log.txt', 'a') as file:
            file.write(f"{username} deposited R{amount}\n")
            deposit_entry.delete(0, tk.END)



# Function to handle withdrawal
def withdraw():
    global balance  
    try:
        amount = int(withdraw_entry.get())
        if amount <= 0:
            raise ValueError("Invalid input, please use positive values")
        
        if amount > balance:
            messagebox.showerror("Error", "Insufficient funds")
        else:
            balance -= amount
            balance_label.config(text=f"Balance: R{balance}")
            with open('transaction_log.txt', 'a') as file:
                file.write(f"{username} withdrew R{amount}\n")
            withdraw_entry.delete(0, tk.END)
    except ValueError as e:
        # messagebox.showerror("Only numbers please... ", str(e))
        messagebox.showerror("Only numbers please... ", "I've been made to track your debts, not sob stories")



# Function to handle logout
def logout():
    global username  
    global balance  

    # Update balance in user_info.txt
    with open('user_info.txt', 'r') as file:
        users = file.readlines()
    with open('user_info.txt', 'w') as file:
        for user in users:
            user_info = user.split(',')
            if user_info[0] == username:
                file.write(f"{username},{user_info[1].strip()},{balance}\n")
            else:
                file.write(user)

    raise_frame(login_frame)

    def generate_pin():
       
        # Initializing our character values
        lowerCase = "abcdefghijklmnopqrstuvwxyz"
        upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%^&*()."
 
        # The string variable is created by concatenating all these character sets
        string = lowerCase + upperCase + numbers + symbols
 
        # The length variable specifies the desired length of the password.
        length = 16
 
        # Randomly shuffle the characters in the string
        shuffled_string = ''.join(random.sample(string, len(string)))
 
        # Randomly select length number of characters from the shuffled string
        password = ''.join(random.sample(shuffled_string, length))
       
        # random_pin = str(random.randint(1000, 9999))
        e3.delete(0, 'end')  # Clear any existing PIN in the entry field
        e3.insert(0, password)  # Insert the generated PIN into the entry field

# Login GUI ===========================================================================================================================================
# Heading for Login Page
login_heading = tk.Label(login_frame, text="Login to Your Account", font=("Arial", 18), bg="#f0f0f0")
login_heading.pack(pady=10)

# Login screen
username_label = tk.Label(login_frame, text="Username", bg="#f0f0f0", font=("Arial", 12))
username_entry = tk.Entry(login_frame)
password_label = tk.Label(login_frame, text="Password", bg="#f0f0f0", font=("Arial", 12))
password_entry = tk.Entry(login_frame, show="*")
login_button = tk.Button(login_frame, text="Login", command=login)
signup_button = tk.Button(login_frame, text="Signup", command=lambda: raise_frame(signup_frame))

username_label.pack(pady=5)
username_entry.pack(pady=5)
password_label.pack(pady=5)
password_entry.pack(pady=5)
login_button.pack(pady=10)
signup_button.pack(pady=5)



# Forgot Password GUI ===========================================================================================================================================
# Create a frame for password reset
reset_password_frame = tk.Frame(root, bg="#f0f0f0")

# Reset Password Page
reset_password_heading = tk.Label(reset_password_frame, text="Reset Password", font=("Arial", 18), bg="#f0f0f0")
reset_password_heading.pack(pady=10)

reset_username_label = tk.Label(reset_password_frame, text="Confirm your username", bg="#f0f0f0", font=("Arial", 12))
reset_username_entry = tk.Entry(reset_password_frame)
reset_password_label = tk.Label(reset_password_frame, text="Create a new Password", bg="#f0f0f0", font=("Arial", 12))
reset_password_entry = tk.Entry(reset_password_frame, show="*")
reset_button = tk.Button(reset_password_frame, text="Reset Password", command=reset_password)

reset_username_label.pack(pady=5)
reset_username_entry.pack(pady=5)
reset_password_label.pack(pady=5)
reset_password_entry.pack(pady=5)
reset_button.pack(pady=10)
forgot_password_button = tk.Button(login_frame, text="Forgot Password", command=forgot_password)
forgot_password_button.pack()



# Signup GUI ===========================================================================================================================================
new_username_label = tk.Label(signup_frame, text="New Username", bg="#f0f0f0", font=("Arial", 12))
new_username_entry = tk.Entry(signup_frame)
new_password_label = tk.Label(signup_frame, text="New Password", bg="#f0f0f0", font=("Arial", 12))
new_password_entry = tk.Entry(signup_frame, show="*")

# Display and Generate PIN
generated_pin_label = tk.Label(signup_frame, text="Generated Password:", bg="#f0f0f0", font=("Arial", 12))
generated_pin_entry = tk.Entry(signup_frame)
 
# e3 = ctk.CTkEntry(frame, show="*")
# e3.grid(row=2, column=1, pady=12, padx=10)
   

create_account_button = tk.Button(signup_frame, text="Create Account", command=signup)
back_button_signup = tk.Button(signup_frame, text="Back to Login", command=go_back_to_login)

new_username_label.pack(pady=5)
new_username_entry.pack(pady=5)
new_password_label.pack(pady=5)
new_password_entry.pack(pady=5)
generated_pin_label.pack(pady=5)
create_account_button.pack(pady=10)
back_button_signup.pack()



# Bankapp GUI ===========================================================================================================================================
welcome_label = tk.Label(bank_frame, text="Welcome to Codex Bank!")
balance_label = tk.Label(bank_frame, text="Balance: R0")  # Display the user's balance
deposit_entry = tk.Entry(bank_frame)  
withdraw_entry = tk.Entry(bank_frame)  
deposit_button = tk.Button(bank_frame, text="Deposit", command=deposit)
withdraw_button = tk.Button(bank_frame, text="Withdraw", command=withdraw) 
logout_button = tk.Button(bank_frame, text="Logout", command=logout)

welcome_label.pack()
balance_label.pack()
deposit_entry.pack()
deposit_button.pack()
withdraw_entry.pack()
withdraw_button.pack()
logout_button.pack()

# Add frames to window
for frame in (login_frame, signup_frame, bank_frame, reset_password_frame):
    frame.grid(row=0, column=0, sticky='news')

# Start on login screen
raise_frame(login_frame)

root.mainloop()
