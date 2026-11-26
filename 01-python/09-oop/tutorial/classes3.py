class Salary():
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Salary: {self.amount} ₺"

    def __repr__(self):
        return f"Salary({self.amount})"

    def __eq__(self, value):
        return self.amount == value.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __add__(self, other):
        self.amount += other.amount
        return self

class Bonus(Salary):
    def __init__(self, amount, type):
        super().__init__(amount)
        self.type = type

    def __str__(self):
        return f"{self.type} bonus: {self.amount} ₺"

    def __repr__(self):
        return f"Bonus({self.amount}, '{self.type}')"

    def __add__(self, other):
        amount_to_add = other.amount 
        if isinstance(other, Bonus):
            self.amount = (self.amount + amount_to_add) * 1.2
        else:
            self.amount += amount_to_add
        return self

# Test 1: Salary
salary1 = Salary(5000)
salary2 = Salary(3000)

print(salary1)  # Salary: 5000 ₺
print(repr(salary1))  # Salary(5000)
print(salary1 == Salary(5000))  # True
print(salary1 < salary2)  # False

sonuc = salary1 + salary2
print(sonuc)  # Salary: 8000 ₺

# Test 2: Bonus
bonus1 = Bonus(1000, "performans")
bonus2 = Bonus(500, "yıllık")
salary3 = Salary(5000)

print("\n--- Bonus Tests ---")
print(bonus1)  # performans bonus: 1000 ₺
print(repr(bonus1))  # Bonus(1000, 'performans')

# Bonus + Bonus = 1.2x
sonuc1 = bonus1 + bonus2
print(sonuc1)  # performans bonus: 1800 ₺

# Bonus + Salary = Normal
bonus3 = Bonus(1000, "performans")
sonuc2 = bonus3 + salary3
print(sonuc2)  # performans bonus: 6000 ₺

# Test 3: Comparison
bonus4 = Bonus(2000, "yıllık")
print(bonus4 < salary1)  # True (2000 < 8000)
print(bonus4 == Bonus(2000, "başka"))  # True (miktara göre)