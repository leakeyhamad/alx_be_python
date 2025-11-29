# bank_account.py

class BankAccount:
    """
    A simple class to represent a bank account with deposit and withdrawal features.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with a starting balance.
        :param initial_balance: The starting balance (default is 0).
        """
        # Encapsulation is achieved by not exposing the balance directly.
        # Although not strictly enforced in Python, using a single underscore 
        # is a convention to denote a protected attribute.
        self._account_balance = initial_balance
        #print(f"Account created with an initial balance of ${self._account_balance:.2f}")

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        :param amount: The amount to deposit.
        """
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the amount from the balance if funds are sufficient.
        :param amount: The amount to withdraw.
        :return: True if withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")