class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance 
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} rupees deposited.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount 
            print(f"{amount} rupees withdrawn.")  # Fixed: removed extra 'f' before {
    
    def get_balance(self):
        return self.balance

account = BankAccount()

while True: 
    print("\nChoose an option:")
    print("a. Deposit")
    print("b. Withdraw")
    print("c. Check Balance")
    print("d. Exit")
    choice = input("Enter your choice (a-d): ")

    if choice == "a":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "b":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "c":
        print("Available balance is:", account.get_balance())
    elif choice == "d": 
        print("Thank you for using the Bank Account program")
        break
    else:
        print("Invalid choice. Please try again.")