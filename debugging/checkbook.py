class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit the specified amount into the checkbook.

        Parameters:
        amount (float): The amount to be deposited.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the checkbook.

        Parameters:
        amount (float): The amount to be withdrawn.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Get the current balance of the checkbook.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        try:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
            if action.lower() == 'exit':
                break
            elif action.lower() == 'deposit':
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            elif action.lower() == 'withdraw':
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            elif action.lower() == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
