from sys import argv

script_name, virabotka, stavka, premiya = argv

print("Имя скрипта: ", script_name)
print("Выработка: ", virabotka)
print("Ставка: ", stavka)
print("Премия, %: ", premiya)


sal = int(virabotka) * int(stavka) * (100 + int(premiya))/100
print(f"Заработная плата сотрудника: {sal}")

# пример ввода в коммандной строке: python task1.py 8 10 11
 