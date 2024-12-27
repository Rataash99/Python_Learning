
def greet(fx):
    def mfx(*args, **kwargs):

        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for being part of this")

    return mfx

@greet
def hello():
    print("hello world")

# @greet
def add(a , b):
    print(f"adding the value of {a} and {b} the result is {a + b}")

greet(add)(2, 8)
