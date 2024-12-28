class Parent:
    def __init__(self, name, habits):
        self.name = name
        self.habits = habits

    def get_details(self):
        print("name :",self.name)
        print("habits :",self.habits)

class Child(Parent):
    def __init__(self, name, habits, occupation):
        super().__init__(name, habits)
        self.occupation = occupation

p = Parent("someone", ["reading newspaper", "tea enthusiast", "loves kachori"])
c = Child("Rohit", ["reading books", "coding", "Biryani"], "python Developer")

print(f"{p.name} loves {p.habits}")
print(f"{c.name} loves {c.habits} and he/she is a {c.occupation}")
