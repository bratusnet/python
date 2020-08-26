# Вывод файла
f = open("file_task3.txt", 'r', encoding="utf-8")
content = f.read()
print(f'Содержимое файла: \n {content}\n')
# Подсчет сотрудников
f = open("file_task3.txt", 'r', encoding="utf-8")
content2 = f.readlines()
print(f'Количество сотрудников - {len(content2)}\n')
# Подсчет слов по строкам
f = open("file_task3.txt", 'r', encoding="utf-8")
total=0
for i in range(len(content2)):
        content3 = f.readline().split()
        total=total+int(content3[1])
        if int(content3[1])<20000:
                print(f'Сотрудник {content3[0]} имеет доход ниже 20тыс равный {content3[1]}')
print(f'\n Средняя величина дохода на сотрудника составлянт: {total/len(content2)}')
f.close()
