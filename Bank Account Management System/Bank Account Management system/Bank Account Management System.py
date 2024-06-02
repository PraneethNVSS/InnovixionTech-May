# Bank Account Management System

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"${amount} withdrawn successfully. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

def create_account():
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")
    return BankAccount(account_number, account_holder)

def main():
    accounts = {}

    while True:
        print("\nBank Account Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account for {account.account_holder} created successfully!")

        elif choice == '2':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account not found.")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
