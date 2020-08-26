f = open("file_task1.txt", 'w', encoding="utf-8")
ln = input('Введите текст \n')
while ln:
    f.write(ln)
    ln = input('Введите текст \n')
    if not ln:
       break
    f.write('\n')
    if not ln:
        break

f.close()
