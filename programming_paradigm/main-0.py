import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")  # <- format with 2 decimals
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")  # <- format with 2 decimals
        else:
            print("Insufficient funds.")
    elif command == "display":
        balance = account.get_balance()
        print(f"Current Balance: ${balance:.2f}")  # <- FIXED HERE
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
