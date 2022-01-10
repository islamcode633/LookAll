n_1,n_2,operat = float(input()),float(input()),str(input())

if((n_2 == 0) and (operat == 'mod' or operat == 'div' or operat == '/')):
    print("Деление на 0!")
    exit()

if(operat == '+' or operat == '-' or operat == '*' or operat == '/'):
    if(operat == '+'):
        print(n_1 + n_2)
    elif(operat == '-'):
        print(n_1 - n_2)
    elif(operat == '*'):
        print(n_1 * n_2)
    else:
        print(n_1 / n_2)

else:
    if(operat == 'mod'):
        print(n_1 % n_2)
    elif(operat == 'pow'):
        print((n_1)**n_2)
    else:
        print(n_1 // n_2)
