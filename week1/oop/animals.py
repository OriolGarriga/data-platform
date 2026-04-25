class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def describe(self):
        print(f"the Animal is called {self.name} and it's {self.age} years old")

    def speak():
        print("...")

class Dog(Animals):
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

    def speak(self):
        print("woof woof")

class Cat(Animals):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("miau")

class Bird(Animals):
    def __init__(self, name, age, beak):
        super().__init__(name, age)
        self.beak = beak

    def speak(self):
        print("chip chip")

if __name__ == "__main__":
    silver = Dog("silver", 8.5, "Schnauzer")
    silver.describe()
