from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, V, H):
        self.V = V
        self.H = H
    
    @abstractmethod
    def sc(self):
        return self.V / 6.5 + 0.5
    @abstractmethod
    def sj(self):
        return self.H * 2 + 0.3

    @property
    def all(self):
        return str(f'Общий подсчет расхода ткани : {round((self.V * self.H),1)}\n ')

class Coat(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.sc = round(self.V/ 6.5 + 0.5,1)

    def __str__(self):
        return f'Расход ткани на пальто : {self.sc}'

    def sc(self):
        return str(f'{self.sc}')
    
    def sj(self):
        return str(f'{self.sj}')


class Jacket(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.sj = round(self.H * 2 + 0.3,1)

    def __str__(self):
        return f'Расход ткани на костюм : {self.sj}'
    
    def sc(self):
        return str(f'{self.sc}')
    
    def sj(self):
        return str(f'{self.sj}')

coat = Coat(8, 2)
jacket = Jacket(2, 0.5)

print(coat)
print(coat.sc)
print(coat.all)


print(jacket)
print(jacket.sj)
print(jacket.all)
