class LivingBeing:
    def __init__(self, type):
        self.type = type

    def is_alive(self):
        return True


class Animal(LivingBeing):
    sleep_hour = 8

    def __init__(self, name, age):
        super().__init__(type="Animal")
        self.name = name
        self.age = age

    def __str__(self):
        return self.info()

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"

    def is_alive(self):
        return super().is_alive()

    def info(self):
        return f"{self.__class__.__name__}'s name: {self.name}, age: {self.age}"

    def sleep_time(self):
        return f"{self.__class__.__name__} sleeps for {self.sleep_hour} hours"


class Dog(Animal):
    sleep_hour = 10

    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

    def info(self):
        animal = super().info()
        return f"{animal}, race: {self.race}"

    def sleep_time(self):
        return super().sleep_time()

    def bark(self):
        return f"{self.name} is barking!"


class Cat(Animal):
    sleep_hour = 16

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def info(self):
        animal = super().info()
        return f"{animal}, color: {self.color}"

    def sleep_time(self):
        return super().sleep_time()

    def meowing(self):
        return f"{self.name} is meowing!"

dog1 = Dog("Boncuk", 5, "Labrador")
cat1 = Cat("Tekir", 3, "Gri")

print(isinstance(dog1, Dog))
print(isinstance(dog1, Animal))
print(isinstance(cat1, Dog))     
print(isinstance(cat1, Animal))   

print(dog1.info())
print(dog1.sleep_time())
print(dog1.bark())
print(cat1.info())
print(cat1.sleep_time())
print(cat1.meowing())