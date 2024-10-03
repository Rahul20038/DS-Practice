class BankLoan():
    def __init__(self, salary, emi):
        self.salary = salary
        self.emi = emi
    def loan(self):
        if self.salary > self.emi:
            print("loan can be approved")
        else:
            print("loan cannot be approved")
rahul = BankLoan(150000,50000)
rahul.loan()