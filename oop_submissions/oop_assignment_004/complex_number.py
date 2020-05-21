import math
class ComplexNumber:
    def __init__(self, real_part = 0, imaginary_part = 0):
        self._real_part = real_part
        self._imaginary_part = imaginary_part
        
        if (type(self._real_part) != int and type(self._real_part) != float) and (type(self._imaginary_part) != int and type(self._imaginary_part) != float):
            raise ValueError("Invalid value for real and imaginary part")
            
        if (type(self._real_part) != int and type(self._real_part) != float):
            raise ValueError("Invalid value for real part")
            
        if (type(self._imaginary_part) != int and type(self._imaginary_part) != float):
            raise ValueError("Invalid value for imaginary part")
        
    @property
    def real_part(self):
        return self._real_part
        
    @property
    def imaginary_part(self):
        return self._imaginary_part
        
    def conjugate(self):
        return ComplexNumber(self._real_part, -self._imaginary_part)
        
    def __str__(self):
        if self._imaginary_part >= 0:
            return f'{self._real_part}+{self._imaginary_part}i'
            
        else:
            return f'{self._real_part}{self._imaginary_part}i'
        
    def __add__(self, complex_number_2):
        
        real = (self._real_part + complex_number_2.real_part)
        
        imaginary = (self._imaginary_part + complex_number_2.imaginary_part)
        
        return ComplexNumber(real, imaginary)
        
    def __sub__(self, complex_number_2):
        
        real = (self._real_part - complex_number_2.real_part)
        
        imaginary = (self._imaginary_part - complex_number_2.imaginary_part)
        
        return ComplexNumber(real, imaginary)
        
    def __mul__(self, complex_number_2):
        
        real = ((self.real_part*complex_number_2.real_part) - (self.imaginary_part*complex_number_2.imaginary_part))
        
        imaginary = ((self._real_part*complex_number_2.imaginary_part) + (self._imaginary_part*complex_number_2.real_part))
        
        return ComplexNumber(real, imaginary)
        
    def __truediv__(self, complex_number_2):
        
        r = float(complex_number_2.real_part**2 + complex_number_2.imaginary_part**2)
        
        real = ((self._real_part*complex_number_2.real_part) + (self._imaginary_part*complex_number_2.imaginary_part))/r
        
        imaginary = ((self._imaginary_part*complex_number_2.real_part) - (self._real_part*complex_number_2.imaginary_part))/r
        
        return ComplexNumber(real, imaginary)
        
    def __abs__(self):
        return round(math.sqrt(self._real_part**2 + self._imaginary_part**2),3)
        
    def __eq__(self, complex_number_2):
        return (self._real_part == complex_number_2.real_part) and (self._imaginary_part == complex_number_2.imaginary_part)