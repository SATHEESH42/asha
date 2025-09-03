class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

def main():
    atm = ATM(100)  # Initial balance
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()