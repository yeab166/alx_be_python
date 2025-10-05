class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        print(f"Current Balance: ${self.__balance:.2f}")
