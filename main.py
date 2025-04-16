# This is a sample Python script.
import sys
from datetime import datetime

class BankAccount:
    """ Represent a Bank"""

    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.trasactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.trasactions.append((datetime.now(),f"Deposited: ${amount:.2f}"))
            print(f"✅ Successfully deposited ${amount:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance.")
        elif amount <= 0:
            print("❌ Withdrawal amount must be greater than 0.")
        else: 
            self.balance -= amount
            self.trasactions.append((datetime.now(), f"Withdrew: ${amount:.2f}"))
            print(f"✅ Successfully withdrew ${amount:.2f}")

    def check_balance(self):
        print(f'Current balance: ${self.balance: .2f}')
    
    def view_transactions(self):
        if not self.trasactions:
            print("📄 No trasactions found.")
        else:
            print("📄 Transaction History:")
            for date, note in self.trasactions:
                print(f" - {date.strftime('%Y-%m-%d %H:%M:%S')} | {note}")    

def main():
    print("Welcome to Bank!")
    name = input("Enter your name to begin:")
    account = BankAccount(name)

    while True:
        print(f'Main Menu')
        print(f'1. Deposit')
        print(f'2. Widthdraw')
        print(f'3. Check Balance')
        print(f'4. View Transactions')
        choice = input('Enter menu item(1-3): ')

        if choice == '1':
            amount = float(input("Enter amount to deposit: $"))
            account.deposit(amount)
        if choice == '2':
            amount = float(input("Enter amount to widthdraw: $"))
            account.withdraw(amount)
        if choice == '3':
            account.check_balance()
        if choice == '4':
            account.view_transactions()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

