class Complex_N:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i \n'

    def __add__(self, other):
        print(f'z1 + z2 :')
        return f'z = {self.a + other.a} + {self.b + other.b} * i \n'

    def __mul__(self, other):
        print(f'z1 * z2 :')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a + self.a * other.b} * i \n'

z1 = Complex_N(5, -6)
z2 = Complex_N(3, 2)
print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)
