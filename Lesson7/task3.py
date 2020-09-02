class Cell:
    def __init__(self, qty):
        self.qty = int(qty)
        
    def __str__(self):
        return f'Количество клеток {self.qty * "*"}'

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        return Cell(self.qty - other.qty) if (self.qty - other.qty) >= 0 else print('Вычитание невозможно, результат меньше нуля!')

    def __mul__(self, other):
        return Cell(int(self.qty * other.qty))

    def __truediv__(self, other):
        return Cell(round(self.qty // other.qty))


    def make_order(self, ncells):
        r = ''
        for i in range(int(self.qty / ncells)):
            r += f'{"*" * ncells} \\n'
        r += f'{"*" * (self.qty % ncells)}'
        return r

cells1 = Cell(12)
cells2 = Cell(15)

print(cells1)
print(cells2)

print(cells1 + cells2)
print(cells1 - cells2)
print(cells1 * cells2)
print(cells1 / cells2)

print(cells1.make_order(5))
print(cells2.make_order(5))
