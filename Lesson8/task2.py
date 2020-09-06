class DivByZero:
    def __init__(self, divid, denom):
        self.divid = divid
        self.denom = denom

    @staticmethod
    def div_zero_exception(divid, denom):
        try:
            return (divid / denom)
        except:
            return (f"Ошибка: деление на ноль !!!")


div = DivByZero(4, 4)
print(DivByZero.div_zero_exception(25, 5))
print(DivByZero.div_zero_exception(5, 0))
