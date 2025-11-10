#we are creating a class with the constructor
# we are also providing default values in class definition init
class person():
    def __init__(self, id=0, name="", email="", active=False):
        # double underscore in python is used to specify something internal of python code
        # 
        #properties or attributes
        self.id = id
        self.name = name
        self.email = email
        self.active = active
        pass

    #indentation is part of how python works. respect it
    #alt key plus arrows allows you to move lines of code up and down
    # alt key + shift up and down copy same line above or below

    #function to be called when a string is passed to print object
    def __str__(self):
        return f"{self.id} - {self.name} - {self.email} - {"Active" if self.active else "Inactive"}"
    
    #equal function
    def __eq__(self,other):
        if self.id == other.id and self.name == other.name and self.email == other.email and self.active == other.active:
            return True
        else:
            return False
        
    #representation function that allows me to print easily lists of stuff
    def __repr__(self):
        return f"[{self.id} - {self.name} - {self.email} - {"Active" if self.active else "Inactive"}]"
    
    def __lt__(self,other):
        #print for debugging
        #print(f"comparing {self.id} with {other.id}")
        return self.id < other.id

if __name__ == "__main__":
    #calling the constructor and have an obejct p of type person
    #objects won't be the same
    p1 = person(1, "Alice", "alice@gmail.com", True)
    p2 = person(1, "Alice", "alice@gmail.com", True)
    
    #objects will be the same
    #p2 = p1
    #print (p1)

    #function call ID to check id of objects
    print(id(p1))
    print(id(p2))


    if p1 == p2:
        print("same")
    else:
        print("different")

