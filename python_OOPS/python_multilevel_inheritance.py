class Grand_Parent:
    def __init__(self, name, habits):
        self.name = name
        self.habits = habits
    
    def print_habits(self):
        print(self.habits)

class Parent(Grand_Parent):
    def __init__(self, name, habits, grand_parent):
        super().__init__(name, habits)
        self.habits.extend(grand_parent.habits)

class Child(Parent):
    def __init__(self, name, habits, parent):
        super().__init__(name, habits, parent)
        self.habits.extend(parent.habits)

gp = Grand_Parent("gp", ["smoking", "reading"])
p = Parent("p", ["reading newspaper", "coffee"], gp)
c = Child("c", ["playing video game", "Programming"], p)

c.print_habits()