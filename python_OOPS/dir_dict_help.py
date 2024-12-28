class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def get_details(self):
        print(f"The name of this person is {self.name}, he/she is {self.age} Yr old and he is a {self.occupation}")
    
    @classmethod
    def from_string(cls, string):
        name, age, occupation = string.split(",")
        return cls(name, int(age), occupation)
    
p1 = Person.from_string("Rohit Singh, 24, Python Developer")

print(f"name : {p1.name}, age : {p1.age}, occupation :{p1.occupation}")

# print(dir(p1))
# print(p1.__dict__)
# print(help(p1))