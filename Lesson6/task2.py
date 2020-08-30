class Road:
    def __init__(self, _length, _width, massa1cm, cm):
        self._length = _length
        self._width = _width
        self.massa1cm = massa1cm
        self.cm = cm

    def massa(self):

        return int(self._length * self._width * self.cm * self.massa1cm /1000)


Massa1 = Road(20, 5000, 25, 5)
print(f'Масса асфальта {Massa1.massa()} т')
