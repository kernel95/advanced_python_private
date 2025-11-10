#type_hints.py


# in this case we are doing some typing doing :str
name:str = "Giuseppe"
#if i say name is 99 I should get an error
name = 99 #you cannot assign number to type string

i = 10
print(i)

#python traditionally isn't strongly typed (means)
i = "ten"
print(i)

#here we are specifying type of name and type of return
def generate_greeting(name:str) -> str:
    return f"Welcome {name}"


i:int
i = generate_greeting(27)

people: list[str]

people = []

people = [1,2,3]