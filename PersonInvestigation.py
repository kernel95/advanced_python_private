
from person import person

#p = person(1, "Alice", "alice@gmail.com", True)

#print (p)


person_list = [person(15, "Alice", "alice@gmail.com", True),
               person(1, "Bob", "bob@gmail.com", False),
               person(1, "Carol", "carol@gmail.com", True),
               person(1, "Dan", "dan@gmail.com", False),]



#lists constructor already has print, just override it

print (person_list)


print (len(person_list))