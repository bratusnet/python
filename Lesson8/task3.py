class Exception_N:
    def __init__(self, *args):
        self.LST = []

    def input_N(self):

        while True:
            try:
                NUM = int(input('Enter number and press Enter : '))
                self.LST.append(NUM)
                print(f'Your list - {self.LST} \n ')
            except:
                print(f"Error - not a number")
                y_or_n = input(f'Try again ? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(self.input_N())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Input finished'
                else:
                    return f'Input finished'

E1 = Exception_N(1)
print(E1.input_N())
