print("Welcome to WhooziJuicy App \n")



codes = [19,28,23,4,78,90,32,54,32,12,67,90,87,6,36,12,24]
codes.sort(reverse=True);


while True:
    try:
       age = int(raw_input('Please enter your age : '))
       break
    except ValueError:
        print "Could you at least give me an actual number?"
        continue

for x in codes :
   
    while type(age) != int or x <> age  :
       while True:
            try:
                age = int(raw_input('Please enter age incorect or skipped queue please try again. : '))
                break
            except ValueError:
                print "Could you at least give me an actual number?"
                continue
       
  
    if age < 18:
         print('No under 18 persons are allowed in the club')
    elif age > 89:
         print('This nightclub is not able to assist persons at the age of 90')
    else :
      print('Welcome to WhooziJuicy enjoy')

    while True:
        try:
           age = int(raw_input('Please enter your age : '))
           break
        except ValueError:
            print "Could you at least give me an actual number?"
            continue
                    
                   
    
    
    
    
    
    
    
