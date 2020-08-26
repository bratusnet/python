dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
newfile = []
with open('file_task4.txt', 'r', encoding="utf-8") as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        newfile.append(dict[i[0]] + '  ' + i[1])
    print(newfile)
with open('new_file_task4.txt', 'w', encoding="utf-8") as file_obj_2:
    file_obj_2.writelines(newfile)
