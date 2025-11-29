# main-0.py

import sys
from bank_account import BankAccount

def main():
    """
    Handles command-line arguments to perform banking operations 
    (deposit, withdraw, display) on a BankAccount object.
    """
    # Initialize a BankAccount instance with an example starting balance
    account = BankAccount(100.00)  

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>[:<amount>]")
        print("Commands: deposit, withdraw (requires :<amount>), display")
        sys.exit(1)

    # The argument is expected in the format "command:amount" or "command"
    parts = sys.argv[1].split(':', 1)
    command = parts[0].lower()
    
    amount = None
    if len(parts) > 1:
        try:
            amount = float(parts[1])
            # Ensure amounts are non-negative for processing
            if amount < 0:
                 raise ValueError("Amount cannot be negative.")
        except ValueError:
            print("Invalid amount provided. Amount must be a positive number.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    
    elif command == "display" and amount is None: # 'display' should not have an amount
        account.display_balance()
    
    else:
        print(f"Invalid command or missing amount for '{command}'.")
        print("Usage: python main-0.py <command>[:<amount>]")

if __name__ == "__main__":
    main()