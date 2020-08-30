from time import sleep

class TrafficLight:
    __color = ['Red', 'Yellow', 'Green', 'Yellow']

    def running(self):
        x = 0
        number_of_cycles=2
        while x < number_of_cycles:
            i = 0
            while i < 4:
                print(f'Color of traffic light: '
                    f'{TrafficLight.__color[i]}')
                if i == 0:
                    sleep(7)
                elif i == 1:
                    sleep(2)
                elif i == 2:
                    sleep(10)
                elif i == 3:
                    sleep(2)
                i += 1
            x += 1


TrafficLight = TrafficLight()
TrafficLight.running()
