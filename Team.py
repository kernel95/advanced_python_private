#Team.py

from person import person


class Team():
    pass

    def __init__(self):
        self.members = []

    def add(self, person):
        self.members.append(person)

    def __str__(self):
        
        " ".join(member.name for member in self)        
        
        #names = ""
        #for member in self.members:
        #    names += f" {member.name} "
        #return names
    
    def __len__(self):
        return len(self.members)
    
    def __iter__(self):
        return iter(self.members)
    
    def __getitem__(self, i):
        return self.members[i]
    

if __name__ == "__main__" :
    
    t = Team()
    t.add (person(9, "Dan", "dan@gmail.com", False))
    t.add (person(15, "alice", "alice@gmail.com", True))
    t.add (person(2, "Carol", "carol@gmail.com", True))
    t.add (person(12, "bob", "bob@gmail.com", False))
    t.add (person(18, "eve", "eve@gmail.com", True))


    print("\n")
    #print(t)
    
    #len won't work straight forward you need to override __len__
    print("\n")
    print(len(t))
    

    for member in t:
        print(member)
    
    print("\n")
    print("*" * 30)
    print (t[0])
    print("*" * 30)
    print(t[-1]) #last one
    print("*" * 30)
    #print from 1 to 3
    print(t[1:3])
    print("*" * 30)
    #print in reverse order
    print(t[::-1])
    print("\n")

    sorted_team = sorted(t)
    print(sorted_team)
    print("\n")
    
    sorted_team = sorted(t, key=lambda member:member.name.upper())
    print(sorted_team)
    print("\n")

    #if you want to add more than one key
    sorted_team = sorted(t, key=lambda member : (member.active, member.name.upper()))
    print(sorted_team)
    print("\n")