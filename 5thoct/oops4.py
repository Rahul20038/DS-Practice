class Employee():
    def __init__(self, empname, empsalary):
        self.empname = empname
        self.empsalary = empsalary
    def Loan(self):
        print("Hello Rahul")
        return f"{self.empname} approved loan, {self.empsalary} Salary."
rahul_emp = Employee("Rahul", 65000)
rahul_emp.Loan()
