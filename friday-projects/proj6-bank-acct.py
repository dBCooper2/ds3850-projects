class BankAccount:
    """
    A class to represent a bank account with basic banking operations
    """
    def __init__(self, account_number, initial_balance=0):
        """
        Initialize bank account with account number and optional initial balance
        """
        self.account_number = account_number
        self.balance = initial_balance
        
    def deposit(self, amount):
        """
        Deposit money into the account
        Returns True if successful, False if invalid amount
        """
        if amount > 0:
            self.balance += amount
            return True
        return False
        
    def withdraw(self, amount):
        """
        Withdraw money from the account
        Returns True if successful, False if invalid amount or insufficient funds
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False
            
    def check_balance(self):
        """
        Return current balance
        """
        return self.balance

def print_menu():
    """
    Display the main menu options
    """
    print("\nPlease choose from the following options:")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Exit")

def get_valid_amount():
    """
    Get and validate a monetary amount from user input
    """
    while True:
        try:
            amount = float(input("Enter amount: $"))
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """
    Main function to run the bank account program
    """
    # Create a bank account
    account = BankAccount("5491647", 0)
    
    print("\nWelcome to the Banking System")
    print("============================")
    
    while True:
        # Verify account number
        entered_account = input("\nPlease enter your account number: ")
        
        if entered_account != account.account_number:
            print("Invalid account number. Please try again.")
            continue
            
        print_menu()
        
        # Get user's choice
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
            
        # Process user's choice
        if choice == 1:  # Deposit
            amount = get_valid_amount()
            if account.deposit(amount):
                print(f"\nDeposit successful!")
                print(f"New balance: ${account.check_balance():.2f}")
            else:
                print("Invalid deposit amount.")
                
        elif choice == 2:  # Withdraw
            amount = get_valid_amount()
            if account.withdraw(amount):
                print(f"\nWithdrawal successful!")
                print(f"New balance: ${account.check_balance():.2f}")
            else:
                print("Insufficient funds or invalid withdrawal amount.")
                
        elif choice == 3:  # Check balance
            print(f"\nCurrent balance: ${account.check_balance():.2f}")
            
        elif choice == 4:  # Exit
            print("\nThank you for using our banking system!")
            print("======================================")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()