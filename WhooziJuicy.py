print("Welcome to WhooziJuicy \n")

age = raw_input('Please enter age code : ')

codes = ['A19','B28','C23','D4','E78','F90','G32','H54','I32','J12','J67','L90','M87','N6','O36','P12','Q24']

for x in codes :
    if age.upper() == 'D4' or age.upper() =='N6' or age.upper() =='P12' or age.upper() =='J12':
        print('No under 18 persons are allowed in the venue')
    elif age.upper() == 'L90' or age.upper() =='F90' :
        print('This nightclub is also not able to assist persons at the age of 90')
    else :
        if age.upper() == x:
            print('Welcome to WhooziJuicy enjoy')
        else:
            while age.upper() != x:
                age = raw_input('Please enter age code again incorect or skipped queue. : ')
                if age.upper() == x:
                    print('Welcome to WhooziJuicy enjoy')
    age = raw_input('Please enter age code : ')

    
    
    
    
    
    
    
