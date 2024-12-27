class Human:
    def __init__(self, _name, _age, _status):
        self.name = _name
        self.__age = _age
        self.status = _status

    

    def get_details(self):
        print(f"The name of the human is {self.name}, he is {self.age} years old and marital status is {self.status}")
    

rohit = Human("Rohit", 24, "single")
print(rohit._Human__age)

        