"""class Employee():
    def __init__(self, empname, empsalary):
        self.empname = empname
        self.empsalary = empsalary
    def Loan(self):
        print("Hello Rahul")
        return f"{self.empname} approved loan, {self.empsalary} Salary."
rahul_emp = Employee("Rahul", 65000)
rahul_emp.Loan()
"""
#Inheritance concept 
class Animal():
    def __init__(self, name):
        self.name = name
    def eat(self):
        return f"{self.name} is Eating."
class Dog(Animal):
    def sound(self):
        return f"{self.name} is Barking."
class Cat(Animal):
    def sound(self):
        return f"{self.name} is Meowing."
class Lion(Animal):
    def sound(self):
        return f"{self.name} is sleeping."
    
dogg = Dog("Tommy")
catt = Cat("Snow bell ")
lion = Lion("Rah")

print(dogg.sound())
print(dogg.eat())
print(catt.sound())
print(catt.eat())
print(lion.sound())
print(lion.eat())