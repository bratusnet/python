class Store:

    def __init__(self, type, name, price, quantity, lists, department, *args):
        self.type = type
        self.department = department
        self.name = name
        self.price = price
        self.quantity = quantity
        self.lists = lists
        self.store_total = []
        self.store = []
        self.units = {'Device type': self.type, 'Device name': self.name, 'Price per unit': self.price, 'Quantity': self.quantity, 'Department': self.department}

    def __str__(self):
        return f'{self.name} price {self.price} quantity {self.quantity}'

    def reception(self):
        units={}
        try:
            unit = input(f'Enter device type (printer/scanner/copier):')
            name = input(f'Enter device name :')
            unit_p = int(input(f'Enter price per unit :'))
            unit_q = int(input(f'Enter quantity :'))
            dep = input(f'Enter department :')
            unique = {'Device type': unit, 'Device name': name,'Price per unit': unit_p, 'Quantity': unit_q, 'Department': dep}
            units.update(unique)
            self.store.append(units)
            print(f'Working list -\n {self.store}')
        except:
            return f'Data entry error !!!'

        print(f'Enter Q to quit or press Enter to proceed...')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.store_total.append(self.store)
            print(f'At the store -\n {self.store_total}')
            return f'Exit'
        else:
            return Store.reception(self)


class Printer(Store):
    def prints(self, color):
        self.color=color
        return f'Printer {self.name} prints {self.lists} lists in {self.color} color.'

class Scanner(Store):
    def scans(self, quality):
        self.quality=quality
        return f'Scanner {self.name} scans {self.lists} lists in {self.quality} resolution.'

class Copier(Store):
    def copies(self):
        return f'Copier {self.name} makes {self.lists} copies.'

p1 = Printer('printer','Xerox', 100, 3, 1000, 'IT')
s1 = Scanner('scanner','Canon', 150, 4, 10000, 'Finance')
c1 = Copier('copier','Brother', 130, 51, 2000, 'HR')

print(p1.prints('green'))
print(s1.scans('high'))
print(c1.copies())

print(p1.reception())
