# by default every attribute is public
# private properties should have a prefix double underscore('__')
# private methods should have prefix double underscore('__') to method name

class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.__salary = salary

    def __getId(self):
        print("id:", self.id)
    

Steve = Employee(3789, 2500)
# Steve.__getName()
Steve._Employee__getId()
print("salary:", Steve._Employee__salary)
# print("id:", Steve.id)
# print("salary:", Steve.__salary)