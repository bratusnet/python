num = int(input("Введите целое положительное число: "))
if num<10:
    print(f"Самая большая цифра в числе: {num}")
elif num==10:
    print(f"Самая большая цифра в числе: 1") 
else:

    result = -1
    while num > 10:
        d = num % 10
        num //= 10
        if d > result:
            result = d
            print(f"Самая большая цифра в числе: {result}")
