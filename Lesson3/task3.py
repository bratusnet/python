def my_func(x1,x2,x3):
    x=[]
    x.append(x1)
    x.append(x2)
    x.append(x3)
    x.remove(min(x))
    return sum(x)

print(my_func(x1=int(input("Введите значение первого аргумента: ")), x2=int(input("Введите значение первого аргумента: ")), x3=int(input("Введите значение первого аргумента: "))))
