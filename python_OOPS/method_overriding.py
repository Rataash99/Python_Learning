class Shape:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def area(self):
        return int(self.x) * int(self.y)

class Circle(Shape):
    def __init__(self, radius, type):
        super().__init__(radius, radius, type)
        self.radius = radius

    def area(self):
        a = 3.14 * super().area()
        print(f"The area of {self.type} is {a}")

rec = Shape(2, 3, "rectangle")
print(f"The area of rectangle is {rec.area()}")

c = Circle(3, "circle")
print(c.area())