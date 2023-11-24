class Fraction:
    def __init__(self,nr,dr=1):
        self.nr = nr
        self.dr = dr
        if dr < 0:
            self.dr = dr*(-1)
            self.nr = nr*(-1)
        self._reduce()

    def show(self):
        print('{}/{}'.format(self.nr, self.dr))

    def multiply(self, x):
        if isinstance(x, int):
            x = Fraction(x)
        y = Fraction(self.nr * x.nr, self.dr * x.dr)
        y._reduce()
        return y

    def add(self, x):
        if isinstance(x, int):
            x = Fraction(x)
        y = Fraction(self.nr*x.dr + x.nr*self.dr , self.dr*x.dr)
        y._reduce()
        return y

    @staticmethod
    def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s
x
    def _reduce(self):
        x = Fraction.hcf(self.nr, self.dr)
        self.nr = self.nr/x
        self.dr = self.dr/x

f1 = Fraction(2,3)
f1.show()
f2 = Fraction(3,4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5) 
f3.show()
f3 = f1.multiply(5) 
f3.show()
