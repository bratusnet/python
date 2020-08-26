try:
    with open('file_task5.txt', 'w+') as file_obj:
        line = input('Введите цифры через пробел \n')
        file_obj.writelines(line)
        my_numb = line.split()

        print(f'Сумма чисел = {sum(map(int, my_numb))}')
except IOError:
    print('Ошибка записи в файл. Ошибка ввода-вывода.')
except ValueError:
    print('Неправильное значение.')
