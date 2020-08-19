def my_user(**kwargs):
    name=input("Введите имя: ")
    second_name=input("Введите фамилию: ")
    date=input("Введите дату рождения: ")
    city=input("Введите город проживания: ")
    email=input("Введите email: ")
    phone=input("Введите телефон: ")

    print(f"Введены данные пользователя {name} {second_name}, дата рождения {date}, проживающего в {city},  email: {email}, телефон: {phone}" )

my_user()
