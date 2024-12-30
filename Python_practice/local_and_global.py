x = 21
print(f"This is the current value of {x}")
def change_val():
    global x
    x = 22

    y = 23
    print(y)

change_val()
print(f"This is the value of {x} after changing it in the function")