# args and kwargs

def fun(*args):
    return sum(args)



print(fun(1, 2, 3, 4))  



def my_fun(**kwargs):
    for key,val in kwargs.items():
        print(f"{key} = {val}")


my_fun(name="John", age=30, city="New York")