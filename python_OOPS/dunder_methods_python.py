class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"id : {self.id}\nname of the employee : {self.name}"

    def __len__(self):
        i = 0
        for ele in self.name:
            i += 1
        
        return i
        
emp1 = Employee("Rohit Singh", 22)

print(emp1)
print(len(emp1))
