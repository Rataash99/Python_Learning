
class Employee:
    def __init__(self, _name, _occupation):
        self.name = _name
        self.occupation = _occupation

    def getDetails(self):
        return [self.name, self.occupation]

rohit = Employee("Rohit", "Developer")

print(rohit.getDetails)


    

