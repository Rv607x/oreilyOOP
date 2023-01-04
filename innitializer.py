class Employee:
    def __init__(self, ID, salary, department):
        self.ID = None
        self.salary = None
        self.department = None

# Creating new object of Employee class with default parameters 
Steve = Employee(3789, 60000, "Human Resources")

#printing properties of Steve

print("Id: ", Steve.ID)
print("Salary: ", Steve.salary)
print("Department: ", Steve.department)