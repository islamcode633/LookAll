#   __________________________ Игра Отгадай Число __________________________
#    
# Правила игры: 
#              - Победитель может быть лишь один
#              - Числа игроков должны отличаться  
#              - Для изменения диапазона чисел требуется два голоса или согласие трех игроков . 
#              - Режим игры "Между Игроками" возможен только для трех игроков
#              - Числовой диапазон должен вкл в себя минимум три числа 
#              - Игрок(и) вводящие числа вне указанного диапозона терят балл в раунде   
#   -------------------------------------------------------------------------
# В игре два режима "с" - игра с комп / "p"- режим между 3-мя игроками . Покинуть игру "exit" или иной символ 
# Начальный диапозон установлен от 1 до 100. Может изменяться игроками по голосованию .
# Игрок нарушевший правила дважды или более теряет один балл за раунд 

import random

  

def f_Repeat(repeat):
    repeat = input('Сыграть c комп введите "c". Режим между игроками "p" . "exit" или любой другой символ для выхода из игры: ')
    return repeat


def iteration_play(valid_value):
    if valid_value == 'exit':
        exit()
    while valid_value == 'c':
        valid_value = game_comp()
    while valid_value == 'p':
        valid_value = game_players()
    return valid_value
    

def game_comp():  
    repeat = ""
    num = int(input('Введите число от 1 до 100  для игры с компьютером:'))
    num_rund = random.randint(1,100)
    if num is num_rund:
        print('You Victory')
        repeat = f_Repeat(repeat)
        return repeat
    else:
        print('You Lose')
        repeat = f_Repeat(repeat)
        return repeat


def game_players():
    repeat = ""
    play1,play2,play3 = int(input('Введите числа от 1 до 100 для Player 1 - ')), int(input('Введите числа от 1 до 100 для Player 2 - ')),int(input('Введите числа от 1 до 100 для Player 3 - '))
    num_rund = random.randint(1,100)
    if (play1 == num_rund) and ((play2 is not play1) and (play2 is not play3) and (play1 is not play3)):
        print('Play 1 Victory !!! Win number - %d' % num_rund)
        repeat = f_Repeat(repeat)
        return repeat
    elif (play2 == num_rund) and ((play2 is not play1) and (play2 is not play3) and (play1 is not play3)):
        print('Play 2 Victory !!! Win number - %d' % num_rund)
        repeat = f_Repeat(repeat)
        return repeat
    elif (play3 == num_rund) and ((play2 is not play1) and (play2 is not play3) and (play1 is not play3)):
        print('Play 3 Victory !!! Win number - %d' % num_rund)
        repeat = f_Repeat(repeat)
        return repeat
    else:
        print('Победитель не выявлен. Хотите переиграть ?')
        repeat = f_Repeat(repeat)
        return repeat
    
    repeat = f_Repeat(repeat)
    return repeat
            

print('Выберите режим игры , где "c" игра с комп , "p" против игроков')
mode_info = input('Введите "c" или "p" - ')

while mode_info == 'c' or mode_info == 'p':
    while mode_info == 'c':
        valid_value =  game_comp()
        mode_info = iteration_play(valid_value)

    while mode_info == 'p':
        valid_value = game_players()
        mode_info = iteration_play(valid_value)











