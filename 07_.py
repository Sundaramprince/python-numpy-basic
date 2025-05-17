# // Creating a class with attributes
class Car:
    color = "red"
    brand = "Toyota"
    
car1= Car()
print(car1.color)
print(car1.brand)

# student class with attributes
class Student:
    name= "SundaramPrince "
    age= 21
    courses= ["Python", "Java", "C++"]
    
s1= Student()
print(s1.name)
print(s1.age)   
print(s1.courses)


    # Creating a class with methods
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


# Example usage
if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)
    account.display_details()
    account.deposit(500)
    account.withdraw(300)
    account.display_details()
    
    
    
            
 
 