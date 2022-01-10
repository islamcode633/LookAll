 ################################
 # Программа  определения кол-ва 
 # автомобилей для перевозки груза 
 ################################

import math


time_work_inday  = int(input("Общее время работы:"))
time_reg_load_unload = int(input("Затраченное время на оформление,загрузка,выгрузка ПС:"))
carrying = int(input("Грузоподъемность авто:"))
value_transportation = int(input("Объем перевозки:"))


numbr_rides = (time_work_inday/time_reg_load_unload) # Кол-во ездок 
perfomance_auto = carrying*numbr_rides # Производительность авто
count_auto = value_transportation/perfomance_auto # кол-во автомобилей
print(math.ceil(count_auto))

input("Для завершения сеанса нажмите любую клавишу:")

