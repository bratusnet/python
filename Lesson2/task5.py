r = [7, 5, 3, 3, 2] # initial rating
print(r)
t=5#у пользователя 5 попыток
while t>0:
    t=t-1
    m = int(input("Введите новый элемент рейтинга: "))
    print(m)
    r.append(m)
    r.sort()
    r.reverse()
    print(r)
    continue

