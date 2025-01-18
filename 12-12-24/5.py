print("Welcome to ABC Bank")
class Bank:
    acbal = 10000
    transaction_count = 0

    def deposit(self):
        dep = int(input("Enter the deposit amount: "))
        if dep < 100:
            print("Amount should be greater than 100")
        elif dep > 50000:
            print("Amount exceeded limit of 50,000")
        elif dep % 100 != 0:
            print("Enter the amount in multiples of 100")
        else:
            Bank.acbal += dep
            print(f"Deposited {dep} successfully. Current balance: {Bank.acbal}")

    def withdraw(self):
        if Bank.transaction_count >= 3:
            print("Maximum number of transactions reached.")
            return

        wit = int(input("Enter the withdrawal amount: "))
        if wit < 100:
            print("Amount should be greater than 100")
        elif wit > Bank.acbal:
            print("Amount exceeds account balance")
        elif wit % 100 != 0:
            print("Enter the amount in multiples of 100")
        elif Bank.acbal - wit < 500:
            print("Need to maintain minimum balance of 500")
        elif wit > 20000:
            print("Transaction limit exceeded. Maximum withdrawal is 20,000")
        else:
            Bank.acbal -= wit
            Bank.transaction_count += 1
            print(f"Withdrawal of {wit} successful. Remaining balance: {Bank.acbal}")

    def balance_enquiry(self):
        print(f"Current balance: {Bank.acbal}")

    def viewOptions(self):
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Enquiry")
        print("4. Exit")
        option = int(input("Choose your option: "))
        return option

    def validate(self):
        attempts = 0
        while attempts < 3:
            pin = int(input("Enter PIN number: "))
            if pin == 1234:
                self.run_operations()
                break
            else:
                attempts += 1
                print("Invalid PIN. Please try again.")
                if attempts == 3:
                    print("Account is locked due to too many failed attempts.")

    def run_operations(self):
        while True:
            option = self.viewOptions()
            if option == 1:
                self.deposit()
            elif option == 2:
                self.withdraw()
            elif option == 3:
                self.balance_enquiry()
            elif option == 4:
                print("Thank you for using ABC Bank. Goodbye!")
                break
            else:
                print("Invalid option, please try again.")
obj = Bank()
obj.validate()
