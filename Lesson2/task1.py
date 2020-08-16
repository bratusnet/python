lst=['Строка',1,2.2,True, ['a'], (9),{1}, {1:'1'}, None]
for i in lst:
    t = type(i)
    print(f"Элемент списка {i} имеет тип {t}")
