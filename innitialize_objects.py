class Employee:
    # id, salary and department are class properties
    ID = None
    salary = None
    department = None

Steve = Employee()

# to access properties of object the dot notation is used
# example is object.property

#printing properties of Steve an object of Employee
print("ID =", Steve.ID)
print("Salary =", Steve.salary)
print("Department =", Steve.department)

# we can also create properties outside of a class 
# this is by assigning values to the object

Steve.ID = 3789
Steve.salary = 60000
Steve.department = "HR"

# we can also create a new proprty outside a class
Steve.title = "Manager"

print("ID =", Steve.ID)
print("Salary =", Steve.salary)
print("Department =", Steve.department)
print("Title: ", Steve.title)