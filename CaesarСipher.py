#_______________ Шифр Цезаря _______________
# Данные для шифрования берутся из указанного файла.

up_registr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_registr = 'abcdefghijklmnopqrstuvwxy'
number = int(input('Введите число шага:'))

summ = ''

def check_char(char):
    if char in up_registr:
        return up_registr[(up_registr.index(char) + number) % len(up_registr)]
    elif char in low_registr:
        return low_registr[(low_registr.index(char) + number) % len(low_registr)]
    else:
        return char 

# За место 'filename.txt' указать имя вашего файла
with open('filename.txt') as myFile:
    for row in myFile:
        for symbol in row:
            summ += check_char(symbol)
print(summ)


input()