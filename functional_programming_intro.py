# fuctional_programming_intro.py


# functions are first-class objects in python

from typing import Callable


def add(a:int, b:int) -> int:
    return a + b


def mul(a:int, b:int) -> int:
    return a * b

def div(a:int, b:int) -> float:
    return a / b

def process(a:int, b:int, func: Callable[[int, int], int]) -> int:
    return func(a, b)

x = 10
y = 20

print (process(x,y,add))
print (process(x,y,mul))
print (process(x,y,div))

#there are different way to define a function
#lambda allows you to create a function like we do with def
sub = lambda x, y : x - y

print(process(x,y,sub))

#define function directly within process
process(x, y, lambda a, b : a* b) # lambda is inline definition of an anonymous function
#lambda is syntax adopted in C# and java world