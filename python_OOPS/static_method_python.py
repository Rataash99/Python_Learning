class Depo:
    def __init__(self, value):
        self.value = value

    def print_val(self):
        print(f"The value provided is {self.value}")

    @staticmethod
    def getDept():
        print("This is a static method!")


depo = Depo("Amazing")
depo.print_val()

Depo.getDept()
depo.getDept()