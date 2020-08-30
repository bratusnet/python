class Car:
    
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    
    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed} km/h'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed} km/h')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than limit for town car'
        else:
            return f'Speed of {self.name} is OK for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed} km/h')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than limit for work car'
        else:
            return f'Speed of {self.name} is OK for work car'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


BMW = SportCar(100, 'Blue', 'BMW', False)
Renault = TownCar(30, 'Black', 'Renault', False)
Toyota = WorkCar(70, 'Red', 'Toyota', False)
Ford = PoliceCar(110, 'White',  'Ford', True)

print(Toyota.turn_right())
print(Renault.turn_left())
print(Ford.police())
print(f'Is {BMW.name} a police car? {BMW.is_police}')
print(f'{Toyota.go()} , {Toyota.show_speed()}')
print(f'{Toyota.name} is {Toyota.color}')


print(BMW.show_speed())
print(Renault.show_speed())

print(Ford.show_speed())
