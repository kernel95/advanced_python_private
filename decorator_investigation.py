#decorators helps to change and touch a function without necessarily changing the original function
def loud(func):
    def wrapper():
        message = func()
        return message.upper()
    return wrapper

@loud
def greet():
    return "hello"

#print(greet())


#decorator that takes parameters

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

#I am not defining a new function
#I am just calling it repeated with a repeating decorator
@repeat(5)
def hello(name):
    print (f"Hello {name}")

hello("Alice")

