class Student():
    def __init__(self, name, number, gpa):
        self.name = name
        self.number = number
        self.gpa = gpa

    def print_info(self):
        return f"Student name {self.name}, number is {self.number}, GPA is {self.gpa}"

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
        return self.gpa

    def congrats(self):
        if self.gpa > 3.5:
            return "GREAT!"
        else:
            return "You can keep working!"

student1 = Student("John", 54321, 3.4)

print(student1.print_info())
print(student1.congrats())
student1.update_gpa(4)
print(student1.print_info())
print(student1.congrats())



class Book():
    def __init__(self, title, page_number, author):
        self.title = title
        self.page_number = page_number
        self.author = author

    def __str__(self):
        return f"{self.title} ({self.author})"

    def __repr__(self):
        return f"Book (title={self.title}, page={self.page_number}, author={self.author})"

    def __eq__(self, value):
        return self.title == value.title

    def __len__(self):
        return self.page_number

    def __lt__(self, other):
        return len(self.page_number) < len(other)

book1 = Book("1984", 328, "George Orwell")
book2 = Book("Donquixote", 752, "Cervantes")

print(book1)
print(repr(book1))
print(book1 == book2)
print(book1 < book2)



class Bank():
    interest_rate = 0.05 # common to all accounts
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient Balance!"

    def apply_interest(self):
        self.balance = self.balance * (1 + self.interest_rate)
        return self.balance

    def info(self):
        return (
            f"--- Account Information ---\n"
            f"Account Number: {self.account_number}\n"
            f"Account Holder: {self.account_holder}\n"
            f"Balance       : ${self.balance}"
        )

account1 = Bank("13579", "Kim", 1000)
account1.deposit(500)
account1.apply_interest()
print(account1.info())