class Fraction:

    def __init__(self,num,denom):
        self.numerator = num
        self.denominator = denom

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self,other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return ((self.numerator==other.numerator) & (self.denominator==other.denominator))


    def __gt__(self,other):
        if (self==other):
            return False
        return (self.numerator/self.denominator > other.numerator/other.denominator)


