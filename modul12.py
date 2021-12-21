
money = int(input("Введите планируемую сумму депозита: "))
fix = 100

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = [ int((per_cent['ТКБ']*money)/fix), int((per_cent['СКБ']*money)/fix),
int((per_cent['ВТБ']*money)/fix), int((per_cent['СБЕР']*money)/fix) ]


print('Максимальная сумма, которую вы можете заработать: %d' % max(deposit))

input()
