# Overloading refers to making a method perform different operations 
# based on the nature of its arguments.

class Employee:
    # defining properties and assigning none to them
    def __init__(self, ID = None, salary = None, department = None):
        self.ID = ID
        self.salary = salary
        self.department = department

    #method overloading
    def demo(self, a, b, c, d=5, e = None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    def tax(self):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)
    
# creating object of Employee class
Steve = Employee()

#printing properties of Steve
print("demo 1")
Steve.demo(1, 2, 3)
print("\n")

print("demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")

print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)