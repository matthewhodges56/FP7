class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited successfully. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")


# Create one bank account
account = BankAccount(account_number=12345678, balance=100)  # You can set an initial balance

# Indefinite loop for user interaction
while True:
    # Ask for account number
    entered_account = int(input("Enter your account number: "))

    if entered_account == account.account_number:
        print("\n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
    else:
        print("Invalid account number. Please try again.")

    print("\n")  # Add a line break for readability in the loop
