def my_div(arg_1, arg_2):
    while True:

        try:
            arg_2 != 0
            print( arg_1 / arg_2)
            break
        except ZeroDivisionError:
            print('Oops! Деление на ноль не допустимо !!!')
            break
        

my_div(arg_1=int(input(f"Введите делимое: ")),
        arg_2=int(input(f"Введите делитель: ")))
