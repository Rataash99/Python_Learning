class Employee:
    company = "Apple"
    def __init__(self, _name):
        self.name = _name

    def get_details(self):
        print(f"The name of the employee is {self.name}, and he works at {Employee.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

ep1 = Employee("Rohit")
ep1.get_details()

Employee.change_company("Google")

ep1.get_details()