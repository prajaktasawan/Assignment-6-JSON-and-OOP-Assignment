class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def bark(self):
        print("Barking: Woof! Woof!")

    def hunt(self):
        print("Hunting: Jack Russell Terriers are known for their hunting skills.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def bark(self):
        print("Barking: Woof!")

    def guard(self):
        print("Guarding: Bulldogs are often used as guard dogs.")


dog1 = Dog("Polo", 3, "Brown")
dog1.description()
dog1.get_info()
print()

terrier = JackRussellTerrier("Juicy", 2, "White and Brown")
terrier.description()
terrier.get_info()
terrier.bark()
terrier.hunt()
print()

bulldog = Bulldog("Rocky", 5, "White")
bulldog.description()
bulldog.get_info()
bulldog.bark()
bulldog.guard()
