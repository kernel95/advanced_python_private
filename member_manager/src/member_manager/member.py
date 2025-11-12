#Member.py

#with this seems everything we did manually here already implements all of those methods
from dataclasses import dataclass

#we use dataclass decorator
@dataclass
class Member():
    id:int
    name:str
    email:str
    active:bool

#don't need init if dataclass used
    #def __init__(self):
        #self.id
        #self.name
        #self.email
        #pass
    
    #this is all I need to unlock sorted for this class items
    def __lt__(self, other):
        return self.id < other.id
    
m1 = Member(1, "Alice", "alice@gmail.com", True)
m2 = Member(1, "Alice", "alice@gmail.com", True)


#print(m1)

members = [m1,m2]

#print(members)


# if m1==m2:
#     print("same")
# else:
#     print("different")