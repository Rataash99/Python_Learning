class Employee:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name of the Employee is {self.name} and he/she is {self.age} Yr old")

    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))
    
emp1 = Employee.from_string("Rohit Singh, 24")

print("\n")
print("name :",emp1.name, "age :",emp1.age)
print("\n")