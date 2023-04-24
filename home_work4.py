revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
employees = int(input('Введите численность сотрудников фирмы: '))
profit = revenue - costs
rent = profit / revenue
salary = profit / employees
while True:
    if revenue > costs:
        print(f'Ура, мы в плюсе, наша прибыль составляет: {profit:.2f}')
        print(f'Рентабельность выручки: {rent:.2f}')
        print(f'Прибыль фирмы в расчете на одного сотрудника: {salary:.2f}')
        break
    elif revenue < costs:
        print(f'Выручка меньше издержок : {profit:.2f},  нужно поднажать!')
        break
    else:
        print(f'Выручка и издержки одинаковы, прибыль равна {profit:.2f}, удачи!')
        break
