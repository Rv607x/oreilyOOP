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


# In the code above, the properties ID and salary and the method displayID()
#  are public as they can be accessed in the class as well as outside the
#  class

print("\n")
#Private attributes cannot be accessed directly from outside the class but can
#  be accessed from inside the class.

class Employee2:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary

Jake = Employee2(2092, 35000)
print("ID:", Jake.ID)
print("Salary:", Jake.__salary) #gives an error because Salary is a private property