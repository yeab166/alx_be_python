# main-0.py

import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        return

    account = BankAccount(100)  # Starting balance
    command_parts = sys.argv[1].split(':')
    command = command_parts[0]
    amount = float(command_parts[1]) if len(command_parts) > 1 else None

    if command == "deposit" and amount:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        print(f"Current Balance: ${account.get_balance()}")
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
