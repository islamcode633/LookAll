#возвращает первый найденный символ(цифру) или 'digit not found'
def search_num(A,B):
    L = list(A)
    i = 0
    while len(A) - i:
        if L[i] == str(B):
            return L[i] 
        i += 1
    else:
        return 'digit not found'   

def integer_of_real(A):
    if A % 2 == 0:
        print('This number integer')
    else:
        print('This number real')


def arifmetic_two_numbrs(A,B,operation):
    if operation == '+': 
        result = A + B
        return result
    elif operation == '*':
        result = A * B
        return result
    elif operation == '/':
        result = A / B
        return result
    elif operation == '-':
        result = A - B
        return result
    else:
        return 0


def number_path(y,x):

    if y == 0 or x == 0:
        print('Centr')
        exit
    else:
        if  y > 0:
            if x > 0:
                print('I')
            else:
                print('II')
        else:
            if y < 0:
                if x < 0:
                    print('III')
                else:
                    print('IV')


def small_two_numbers(A,B):
    if A < B:
        small = A
        return small
    elif B < A:
        small = B
        return small
    else:
        print('Числа равны')

#################################
def small_of_free_numbers(A,B,C):
    if A < B and A < C:
       small = A 
       return small
    elif B < A and B < C:
       small = B 
       return small
    elif C < B and C < A:
       small = C 
       return small
    else:
       return small_free_num(A,B,C)    
# наименьшее из трех чисел ,где два равны между собой      
def small_free_num(A,B,C):
    if A == B and A < C:
       small = A
       return small         
    elif B == C and B < A:
       small = B
       return small
    else:
       small = C
       return small
##################################

def cube_body(body_long,body_height,body_width):
    body_volume = body_long * body_height * body_width
    return body_volume


def summ_args(*nums):
    all_summ = 0
    for x in nums:
        all_summ += x
    return all_summ


def multiply(*nums):
    all_multi = 1
    for x in nums:
        all_multi *= x
    return all_multi

    