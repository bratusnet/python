
v = int(input("Введите значени выручки, руб: "))
i = int(input("Введите значени издержек, руб: "))
pribil=v-i
p=abs(pribil)
rent=pribil/v

if pribil<0:
    print(f"Убыток фирмы: {p} руб")
else:
    print(f"Прибыль фирмы: {pribil} руб")
    print(f"Рентабильность фирмы: {rent}")
ch = int(input("Введите численность сотрудников фирмы: "))
ps=pribil/ch
while num > 10:
    d = num % 10
    num //= 10
    if d > result:
        result = d




