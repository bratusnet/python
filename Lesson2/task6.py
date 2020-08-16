# Ввод информации о товарах
n = int(input("Введите количество вводимых товаров: "))
n2=n
c=1
mylist=[]
while n>0:
    name = input(f"Введите название товара {c}: ")
    price = input(f"Введите цену товара {c}: ")
    quant = input(f"Введите количество товара {c}: ")
    ed = input(f"Введите единицу {c}: ")
    my_dict = dict(Name=name, Price=price, Quantity=quant, Meas=ed )
    mytuple=(c,my_dict)
    mylist.append(mytuple)
    n = n - 1
    c=c+1
    continue
 
print(f"Результат ввода товаров: {mylist}")
# Аналитика
c2=0
L1=[]
L2=[]
L3=[]
L4=[]
dict2 = dict(название=L1, цена=L2, количество=L3, ед=L4 )

for i in range(1, len(mylist)+1, 1):
    l11=mylist[i-1][1]['Name']
    l12=mylist[i-1][1]['Price']
    l13=mylist[i-1][1]['Quantity']
    l14=mylist[i-1][1]['Meas']

    L1.append(l11)
    L2.append(l12)
    L3.append(l13)
    L4.append(l14)
print(f"Результат проведенной аналитики: {dict2}")    
