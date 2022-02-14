##
#~~~~~~~ A program for finding in which quarter a figure is located by its coordinate
   

coordinate = (input('Enter shape coordinates: '))

if len(coordinate) == 2 and coordinate[0] in 'abcdefgh' and coordinate[1] != '9':  
    def one_quarter(coordinate):
        for x in 'abcd':
            if  coordinate[0] in x:   
                literal_base = coordinate[0]
                break
        else:
            literal_base = 0
    
        for x in '1234':
            if coordinate[1] in x:
                number_basis = coordinate[1]
                break
        else:
            number_basis = 0 
    
        if literal_base and number_basis:
            return 'First Quarter'
        else:
            return two_quarter(coordinate)

    def two_quarter(coordinate):
        for x in 'efgh':
            if coordinate[0] in x:
                literal_base = coordinate[0]
                break
        else:
            literal_base = 0
    
        for x in '1234':
            if coordinate[1] in x:
                number_basis = coordinate[1]
                break
        else:
            number_basis = 0
        if literal_base and number_basis:
            return 'Two Quarter'
        else:
            return free_quarter(coordinate)
        
    def free_quarter(coordinate):
        for x in 'abcd':
            if coordinate[0] == x:
                literal_base = coordinate[0]
                break
        else:
            literal_base = 0 

        for x in '5678':
            if coordinate[1] == x:
                number_basis = coordinate[1]
                break
        else:
            number_basis = 0
        if literal_base and number_basis:
            return 'Free Quarter'
        else:
            return four_quarter(coordinate)

    def four_quarter(coordinate):
        for x in 'efgh':
            if coordinate[0] in x:
                literal_base = coordinate[0]
                break
        else:
            literal_base = 0
    
        for x in '5678':
            if coordinate[1] in x:
                number_basis = coordinate[1]
                break
        else:
            number_basis = 0
        if literal_base and number_basis:
            return 'Four Quarter'
        else:
            return 'Invalid Figure Сoordinate'
    print(one_quarter(coordinate))
else:
    print('Not Valid Data')
