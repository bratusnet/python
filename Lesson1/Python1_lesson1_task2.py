
num = int(input("Введите время в секундах: "))

hour=num//3600
min=num%3600//60
sec=num%3600%60

print(f"Время: {hour}: {min}: {sec}")


