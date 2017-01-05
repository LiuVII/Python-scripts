import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        re = self.real + no.real
        im = self.imaginary + no.imaginary
        return Complex(re, im)

    def __sub__(self, no):
        re = self.real - no.real
        im = self.imaginary - no.imaginary
        return Complex(re, im)

    def __mul__(self, no):
        re = self.real * no.real - self.imaginary * no.imaginary
        im = self.imaginary * no.real + self.real * no.imaginary
        return Complex(re, im)

    def __truediv__(self, no):
        nosqr = (no.mod()).real ** 2
        re = (self.real * no.real + self.imaginary * no.imaginary) / nosqr
        im = (self.imaginary * no.real - self.real * no.imaginary) / nosqr
        return Complex(re, im)

    def mod(self):
        re = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        im = 0
        return Complex(re, im)

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
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
