class BmiCalc():
    def __init__ (self, weight, height):
        self.weight = weight
        self.height = height
    def bmi(self):
        BMI = self.weight/self.height*self.height
        if BMI < 18.5:
            print("Less Weight")
        elif BMI > 18.5 and BMI < 24.99 :
            print("Normal weight")
        elif BMI > 25.0 and BMI < 30.0:
            print("Heavy weight")
        else:
            print("obesity")
rahul = BmiCalc(75, 1.79)
rahul.bmi()