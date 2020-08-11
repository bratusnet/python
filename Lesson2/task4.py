m = input("Введите несколько слов: ")
m1=m.split(' ')
for i in range(1, len(m1)+1, 1):
    res = m1[i - 1][:10]
    print(res)
