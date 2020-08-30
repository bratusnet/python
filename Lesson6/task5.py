class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбран предмет: {self.title}. --Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Ваш выбор: {self.title}. --Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вам достался: {self.title}. --Запуск отрисовки маркером'


pen_1 = Pen('Ручка')
pencil_1 = Pencil('Карандаш')
handle_1 = Handle('Маркер')
print(pen_1.draw())
print(pencil_1.draw())
print(handle_1.draw())

