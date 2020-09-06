class Data:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def izvlek(cls, dd_mm_yyyy):
        date = []
        for i in dd_mm_yyyy.split():
            if i != '-': date.append(i)
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2050 >= year >= 0:
                    return f'Валидация формата даты прошла успешно.'
                else:
                    return f'Введено недопустимое значение года !!!'
            else:
                return f'Введено недопустимое значение месяца !!!'
        else:
            return f'Введено недопустимое значение дня !!!'

    def __str__(self):
        return f'Введена дата {Data.izvlek(self.dd_mm_yyyy)}'


d1 = Data('04 - 08 - 2020')
print(d1)
print(d1.izvlek('09 - 09 - 1999'))
print(Data.valid(12, 12, 2022))
print(Data.valid(21, 13, 2011))
print(Data.valid(32, 11, 2000))
print(Data.valid(23, 10, 3000))
