class Animal:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print(f"{self.name} is making a strange noise.")

# Dog subclass
class Dog(Animal):
    def make_noise(self):
        print(f"{self.name} is barking.")

# Bird subclass
class Bird(Animal):
    def make_noise(self):
        print(f"{self.name} is tweeting.")

# Snake subclass 
class Snake(Animal):
    def make_noise(self):
        print(f"{self.name} is hissing.")

dog = Dog("Sparky")
bird = Bird("Tweety")
snake = Snake("Slither")

animals = [dog, bird, snake]
for x in animals:
    x.make_noise()
