class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    
    def dance_name(self):
        self.dance

class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance):
        self.dance = dance
        self.name = name

emp1 = DancerEmployee("Rohit", "break")

print(f"the name is {emp1.name} and he knows {emp1.dance} dance")

emp1.get_name()