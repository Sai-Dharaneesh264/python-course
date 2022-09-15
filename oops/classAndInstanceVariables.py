class Employee:

    def __init__(self, id=None, salary=None, department=None):
        self.id = id
        self.salary = salary
        self.department = department
    
    def tax(self):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)
    
    def demo(self, a, b, c, d=5, e=None):
        print(a, b, c, d, e, sep=", ")



Steve = Employee(3789, 2500, "Human Resources")

print("id = ", Steve.id)
print("salary:", Steve.salary)
print("Department:", Steve.department)
print("Tax paid by Steve:", Steve.tax())
print("Salary per day of Steve:", Steve.salaryPerDay())

print(Steve.demo(1, 2, 3))
print(Steve.demo(1, 2, 3, 4))
print(Steve.demo(1, 2, 3, 4, 5))