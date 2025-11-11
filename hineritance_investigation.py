#hineritance_investigation.py

# OO feature
#Abstraction
#Encapsulation
#Inheritance
#Polymorphism

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(f"Person: {self.first_name} {self.last_name}")
            

#Employee object will be based on person class like extends
class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id

    def display(self):
        super().display()
        print(f"EmployeeId: {self.employee_id}")
        
            


e = Employee("Alice", "Adams", "E12345")
e.display()
