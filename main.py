# список банков со ставками по депозитам
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# ввод суммы депозита
money = input("введите сумму желаемого депозита (руб.):")

# здесь будем хранить рассчет депозитных значений по всем банкам
deposit = []

'''теперь создадим список с рассчитанными значениями депозита для каждого банка,
воспользовавшиcь циклом for для словаря per_cent'''
for bank_name, bid in per_cent.items():
    deposit.append((bid * int(money)/100))

# теперь найдем максимальное значение депозита и выведем его на экран
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
