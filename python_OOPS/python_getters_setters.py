class MyClass:
    def __init__(self, _value):
        self.value = _value

    def show(self):
        print(f"value is {self.value}")
    
    @property
    def ten_value(self):
        return 10 * self.value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self.value = new_value / 10

    
new_obj = MyClass(3)
new_obj.show()

# getting the value 
print(new_obj.ten_value)

# setting the value
new_obj.ten_value = 8
print(new_obj.ten_value)

    