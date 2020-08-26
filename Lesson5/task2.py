# Вывод файла
f = open("file_task2.txt", 'r', encoding="utf-8")
content = f.read()
print(f'Содержимое файла: \n {content}\n')
# Подсчет строк
f = open("file_task2.txt", 'r', encoding="utf-8")
content2 = f.readlines()
print(f'Количество строк - {len(content2)}\n')
# Подсчет слов по строкам
f = open("file_task2.txt", 'r', encoding="utf-8")
for i in range(len(content2)):
        content3 = f.readline()
        content3 = content3.split()
        print(f'Количество слов строки {i + 1} -  {len(content3)}')

f.close()
