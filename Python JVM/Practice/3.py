# decorators

def greet(fx):
    def mfx():
        print("Good morning, thanks for using this function")
        print(fx())
        print("Thanks for using this function")
    return mfx


@greet
def hello():
    return "Hello, world!"

hello()