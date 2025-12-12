print("NGÔ ĐỨC ĐAI")
print("msv:245751030110007")
print("################################")
print("6)")
class IOString:
    def __init__(self):      
        self.str1 = "" 
    def get_String(self):
        self.str1 = input("Nhập chuỗi của bạn: ")
    def print_String(self):
        print(self.str1.upper())
if __name__ == "__main__":
    str1_instance = IOString()
    str1_instance.get_String()
    str1_instance.print_String()
print("7)")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius
c = Circle(5)
print("Diện tích:", c.area())
print("Chu vi:", c.circumference())
print("8)")
class Bank:
    Account_type = "Savings"
    location = "Guntur"
    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.Account_type
        self.location = Bank.location
    def __repr__(self):
        print("Welcome to the SBI ATM Machine")
        print("------------------------------------")
        account_pin = int(input("Please enter your pin number: "))
        if account_pin == 160206:
            self.Account()
        else:
            print("Pin Incorrect. Please try again")
            self.Error()
        return ' '.join([self.name, self.Account_Number])
    def Error(self):
        account_pin = int(input("Please enter your pin number: "))
        if account_pin == 160206:
            self.Account()
        else:
            print("Pin Incorrect. Please try again")
            self.Error()
    def Account(self):
        print("Your Card Number is: XXXX XXXX XXXX 1337")
        print("Would you like to deposit / withdraw / check balance?")
        print("""
1) Balance
2) Withdraw
3) Deposit
4) Quit
""")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Your balance is:", self.balance)
            self.Account()
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdraw successful! New balance:", self.balance)
            else:
                print("Insufficient funds!")
            self.Account()
        elif choice == 3:
            amount = float(input("Enter amount to deposit: "))
            self.balance += amount
            print("Deposit successful! New balance:", self.balance)
            self.Account()
        elif choice == 4:
            print("Thank you for using SBI ATM!")
        else:
            print("Invalid choice. Try again.")
            self.Account()
user = Bank("An User", "1234-5678-9999", 5000)
print(user)






