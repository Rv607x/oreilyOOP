# Public attributes are those that can be accessed inside the class and 
# outside the class.
# example of public attribute 

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID 
        self.salary = salary

    def displayID(self):
        print("ID: ", self.ID)

Steve = Employee(3737, 25000)
Steve.displayID()
print(Steve.salary)