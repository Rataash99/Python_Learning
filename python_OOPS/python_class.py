class Student:
    roll_no = -1
    name = "Rohit"
    standart = 8
    subjects = ["maths", "chemistry", "physics", "english", "Physical Education"]
    section = "B"


    def get_details(self):
        return [self.roll_no, self.name, self.standard, self.subjects, self.section]        

rohit = Student()
rohit.roll_no = 22
rohit.name = "rohit"
rohit.standard = 11
rohit.section = "A"

details = rohit.get_details()
print(details)


    

