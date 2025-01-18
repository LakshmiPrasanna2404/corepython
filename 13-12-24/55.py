import streamlit as st

st.title("Welcome to ABC Bank")

class Bank:
    def __init__(self):
        # Initialize account balance and transaction count as instance variables
        self.acbal = 10000
        self.transaction_count = 0

    def deposit(self):
        # Deposit function with validations
        dep = st.number_input("Enter the deposit amount:", key="deposit_amount")
        if dep < 100:
            st.error("Amount should be greater than 100")
        elif dep > 50000:
            st.error("Amount exceeded limit of 50,000")
        elif dep % 100 != 0:
            st.error("Enter the amount in multiples of 100")
        else:
            self.acbal += dep
            st.success(f"Deposited {dep} successfully. Current balance: {self.acbal}")

    def withdraw(self):
        # Withdrawal function with validations
        if self.transaction_count >= 3:
            st.write("Maximum number of transactions reached.")
            return

        wit = st.number_input("Enter the withdrawal amount:", key="withdraw_amount")
        if wit < 100:
            st.error("Amount should be greater than 100")
        elif wit > self.acbal:
            st.error("Amount exceeds account balance")
        elif wit % 100 != 0:
            st.error("Enter the amount in multiples of 100")
        elif self.acbal - wit < 500:
            st.error("Need to maintain minimum balance of 500")
        elif wit > 20000:
            st.error("Transaction limit exceeded. Maximum withdrawal is 20,000")
        else:
            self.acbal -= wit
            self.transaction_count += 1
            st.success(f"Withdrawal of {wit} successful. Remaining balance: {self.acbal}")

    def balance_enquiry(self):
        # Display current balance
        st.write(f"Current balance: {self.acbal}")

    def viewOptions(self):
        # Display options menu
        st.write("1. Deposit")
        st.write("2. Withdraw")
        st.write("3. Balance Enquiry")
        st.write("4. Exit")
        option = st.number_input("Choose your option:", key="operation_choice")
        return option

    def validate(self):
        # PIN validation with 3 attempts
        attempts = 0
        while attempts < 3:
            pin = st.text_input("Enter PIN number:", type="password", key="pin_input")
            if pin == "1234":
                self.run_operations()
                return
            else:
                attempts += 1
                st.error("Invalid PIN. Please try again.")
                if attempts == 3:
                    st.error("Account is locked due to too many failed attempts.")
                    return

    def run_operations(self):
        # Running operations in a loop
        while True:
            option = self.viewOptions()
            if option == 1:
                self.deposit()
            elif option == 2:
                self.withdraw()
            elif option == 3:
                self.balance_enquiry()
            elif option == 4:
                st.success("Thank you for using ABC Bank. Goodbye!")
                break
            else:
                st.error("Invalid option, please try again.")
obj = Bank()
obj.validate()
