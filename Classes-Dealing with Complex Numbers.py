import math
class Complex(object):
    def __init__(self,real,imagine):
        self.real=real
        self.imagine=imagine
    def __add__(self,num):
        return Complex(self.real + num.real , self.imagine + num.imagine)
    
    def __sub__(self,num):
        return Complex(self.real - num.real , self.imagine - num.imagine)
    def __mul__(self, num):
        p = complex(self.real , self.imagine)*complex(num.real , num.imagine)
        return Complex(p.real , p.imag)

    def __truediv__(self, no):
        div = complex(self.real , self.imagine)/complex(no.real , no.imagine)
        return Complex(div.real , div.imag) 
    def mod(self):
        m = math.sqrt(self.real**2 + self.imagine**2)
        return Complex(m,0)

 
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result    
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y,x-y,x,x*y,x/y]), sep='\n')