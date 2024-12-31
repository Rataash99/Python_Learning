class Animal:
    def __init__(self, sound, breed):
        self.sound = sound
        self.breed = breed

    def make_sound(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self, name):
        super("Woof-Woof", self.breed)
        self.name = name

    def make_sound(self):
        print("Woof-Woof")

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Meow-Meow")

dog = Dog("dogo")
print(dog.name)
print(dog.breed)
dog.make_sound()

cat = Cat("kitty")
print(cat.name)
cat.make_sound()