# Первый вариант
def my_func(x,y):
    return x**y

print(my_func(x=int(input("Введите действительное положительное число: ")), 
y=int(input("Введите целое отрицательное число: "))))

# Второй вариант
def my_func(x,y):
    res=1
    for i in range(abs(y)):
        res=res/x
    return res

print(my_func(x=int(input("Введите действительное положительное число: ")), 
y=int(input("Введите целое отрицательное число: "))))
