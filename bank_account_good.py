class BankAccount:
    """Represents a bank account with deposit and withdrawal capabilities."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add money to the account."""
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraw money if sufficient funds are available."""
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds!")

    def display_balance(self) -> None:
        """Display the current balance."""
        print(f"Balance for {self.owner}: {self.balance}")

    def owner_details(self) -> None:
        """Display the account owner's name."""
        print(f"Account owner: {self.owner}")
