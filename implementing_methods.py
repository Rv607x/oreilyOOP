class Employee:
    def __init__(self, ID = None, salary = None, department = None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):
        return (self.salary * 0.3)

    def salaryPerDay(self):
        return (self.salary / 30)


Steve = Employee(3789, 60000, "Human Resources")

print("ID: ", Steve.ID)
print("Department: ", Steve.department)
print("Tax per Month: ", Steve.tax())
print("Salary per Month: ", Steve.salary)
print("Salary per Day: ", Steve.salaryPerDay())
