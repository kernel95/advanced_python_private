#sorting_investigation.py


from person import person


names = ["giuseppe", "tracy", "mary", "alice", "dan", "bob", "eve", "Alice"]
#print(names)

names.sort()
#print(names)

names.sort(reverse=True)
#print(names)
#print("\n")

print("\n")
def to_upper(name:str) -> str:
    return name.upper()

names.sort(key=to_upper)
#print(names)

#use lambda
names.sort(key=lambda name: name.upper(), reverse=True)
#print(names)

people = [
    person(15, "Alice", "alice@gmail.com", True),
    person(12, "Bob", "bob@gmail.com", False),
    person(2, "Carol", "carol@gmail.com", True),
    person(9, "Dan", "dan@gmail.com", False),
    person(10, "alice", "alice@gmai.com", True)
]

def get_sort_key(person):
    return person.id

def sort_name_key(person):
    return person.name

people.sort(key=get_sort_key)
#print(people)
#print("\n")

people.sort(key=sort_name_key)
#print(people)
#print("\n")

#you can use lambda instead of definying functions and they stay anonymous
people.sort(key=lambda person: person.id)
#print(people)
#print("\n")

#sort purposes
#function called sorted and it is a source of confusion
sorted_names = sorted(names)
print(sorted_names)
print("\n")

#upper is for case insensitive
sorted_names = sorted(names, key=lambda name:name.upper())
print(sorted_names)
print("\n")

#i want to sort a list of objects
#need to add a def __lt__ to compare the id in the person.py file
sorted_members = sorted(people)
print(sorted_members)
print("\n")

sorted_by_names = sorted(people, key=lambda person:person.name.upper())
print(sorted_by_names)
print("\n")

#collapsing everything in a print 
#very pythonic
print("\n".join([person.name for person in sorted_by_names]))
print("\n")

#active_people = [person for person in sorted_by_names if person.active]
#print("\n".join([person in active_people]))

people_tuple = ("Zoe", "Yvonne", "Alice")
#oes not have iteraable but can be sorted
sorted_people_tuple = sorted(people_tuple)
print(sorted_people_tuple)
print("\n")

