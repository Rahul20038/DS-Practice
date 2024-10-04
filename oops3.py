class Experince:
    """ Encapsulation get & set & propertys"""
    def __init__ (self, Exp):
        self._Exp = Exp
    
    @property
    def Exp(self):
        print("execute getter")
        return self._Exp
    @Exp.setter
    def Exp(self, new_exp):
        print("Execute setter")
        if isinstance(new_exp, float) and new_exp > 0:
            self._Exp = new_exp
        else:
            print("Enetr valid salary")
rahul_exp = Experince(5)
print(rahul_exp.Exp)
rahul_exp.Exp = 6.0
print(rahul_exp.Exp)