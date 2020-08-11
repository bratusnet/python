
num = int(input("Введите целое положительное число: "))


result = -1
while num > 10:
    d = num % 10
    num //= 10
    if d > result:
        result = d


print(f"Результат: {result}")


