pin = 1233

# Function to read balance from a file
def read_balance():
    try:
        with open('balance.txt', 'r') as file:
            balance = float(file.read())
    except FileNotFoundError:
        balance = 20000  # Default balance if file does not exist
    return balance

# Function to save balance to a file
def save_balance(balance):
    with open('balance.txt', 'w') as file:
        file.write(str(balance))

def authentication():
    attempt = 3
    while attempt > 0:
        entered_pin = int(input("Please enter your PIN: "))
        if entered_pin == pin:
            print("Authentication Successful!!")
            return True              
        else:
            attempt -= 1              
            print(f"Incorrect PIN, you have {attempt} attempts left")
            
    return False

def check_balance(balance):
    print(f"Your current balance is: ${balance}")

def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        balance += amount
        save_balance(balance)  # Save updated balance to file
        print(f"Deposit successful!! Your new balance is: ${balance}")
    else:
        print("Invalid deposit amount")
    return balance

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if 0 < amount <= balance:
        balance -= amount
        save_balance(balance)  # Save updated balance to file
        print(f"Withdrawal successful!! Your current balance is: ${balance}")
    elif amount > balance:
        print("Insufficient balance")
    else:
        print("Invalid withdrawal amount")
    return balance

def atm_menu():
    balance = read_balance()  # Read balance from file at start
    while True:
        print("\n.......ATM Menu.....")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = int(input("Please choose an option: "))
        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            balance = deposit(balance)  # Update balance after deposit
        elif choice == 3:
            balance = withdraw(balance)  # Update balance after withdrawal
        elif choice == 4:
            print("Thank you for using the ATM, Have a nice day!!")
            break
        else:
            print("Invalid option, please try again")

if authentication():
    atm_menu()
else:
    print("Incorrect attempt, exiting the session...")
