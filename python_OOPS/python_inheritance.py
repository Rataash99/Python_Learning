class Employee:
    def __init__(self, _id, _name, _occupation):
        self.id = _id
        self.name = _name
        self.occupation = _occupation

    def show_details(self):
        print(f"Employee details are :- \nid : {self.id} \nname : {self.name} \noccupation : {self.occupation}" )

class Programmer(Employee):
    # def __init__(self, _language):
    #     self.language = _language

    def show_language(self):
        print(f"{self.name} uses {self.language}")

em = Employee("2EA", "Rohit","Programmer")
em.show_details()

prg = Programmer("2EA", "Rohit","Programmer")
prg.show_details()
