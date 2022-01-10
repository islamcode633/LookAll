count_ticket = int(input('Желаемое кол-во билетов: '))
age = []

if count_ticket:
    for x in range(count_ticket):
        i = int(input('Введите возраст посетителя: '))
        age.append(i)
else:
    exit()

sum_ticket = 0
for x in range(count_ticket):
    if 14 < age[x] < 18:
        print(f'Билет №{x+1} Можете пройти бесплатно')
    elif 18 <= age[x] <= 25:
        print(f'Билет №{x+1} cтоимость: 990р')
        sum_ticket +=  990 
    elif 25 < age[x] < 60:
        print(f'Билет №{x+1} cтоимость: 1390')
        sum_ticket += 1390
else:
    if 3 < count_ticket:
        sum_ticket -= (sum_ticket/ 10)
        print(f'Полная стоимость с 10% скидкой: {sum_ticket}')
    else:
        print(f'Полная стоимость составила: {sum_ticket}')


