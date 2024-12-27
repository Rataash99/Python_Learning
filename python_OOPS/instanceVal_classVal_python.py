class Human:
    population = 0

    def __init__(self, _name, _country, _city, _age, _marital_status):
        self.name = _name
        self.country = _country
        self.city = _city
        self.age = _age
        self.marital_status = _marital_status
        Human.population += 1

    def get_details(self):
        details = [self.name, self.city, self.country, self.marital_status]
        for field in details:
            print(field)

human1 = Human("Rohit", "India", "Delhi", 24, "single")
human2 = Human("Nitin", "India", "Delhi", 22, "single")

human1.get_details()
human2.get_details()

print(Human.population)


