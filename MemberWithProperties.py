# MemberWithProperties.py


from dataclasses import dataclass

#_age is a convention to say it is a property encapsulated

@dataclass
class Member():
    id:int
    name:str
    email:str
    active:bool
    _age:int

    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Invalid age {value}")
        self._age = value

    
m = Member(1, "Alice", "alice@gmail.com", True, 29)
print(m)

#what about encapsulation?
#encapsualtion to prevent to do illegal things encapsulated in the class
#we use another decorator which is @propert and we do a def

m.name = "Changed"
#m._age = -99
m.age = -99
print(m.age)

