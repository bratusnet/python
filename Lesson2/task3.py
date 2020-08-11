#через dict
while True:
    m = int(input("Введите номр месяца в виде целого числа от 1 до 12: "))
    if m > 12 or m < 0: continue
    dict={1:'Winter',2:'Winter',12:'Winter',
    3:'Spring',4:'Spring',5:'Spring',
    6:'Summer',7:'Summer',8:'Summer',
    9:'Autumn',10:'Autumn',11:'Autumn',}
    s = dict.get(m)
    print(f"Ваше время года: {s}")
    break
#через list
while True:
    m = int(input("Введите номр месяца в виде целого числа от 1 до 12: "))
    if m > 12 or m < 0: continue
    season=['Winter','Spring','Summer','Autumn']
    if m in [1,2,12]:print(f"Ваше время года: {season[0]}")
    elif m in [3,4,5]:print(f"Ваше время года: {season[1]}")
    elif m in [6, 7, 8]:print(f"Ваше время года: {season[2]}")
    else: print(f"Ваше время года: {season[3]}")
    break
