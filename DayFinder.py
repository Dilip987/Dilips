
'''Once you entered the date it will tell you the weekday'''

## Ask for the user name to greet
x=input('Please enter your name:')
print('Hi!,',x)

import datetime

while True:
    day=input('Please enter a date (like 2099,12,23) or q to exit:')
    
    ## check whether the user wants to quit or not
    if day.lower()=='q':
        break
    
    ## check for the weekdays
    def is_weekend(day):
        try:
            day=datetime.datetime.strptime(day,'%Y,%m,%d')
        except Exception:
            print('Please enter the date in the format year,month,date or q to exit.\n ')
        else:
            if day.weekday()==0:
                print(day,' is Monday\n')
            elif day.weekday()==1:
                print(day,'is Tuesday\n')
            elif day.weekday()==2:
                print(day,'is Wednesday\n')
            elif day.weekday()==3:
                print(day,'is Tuesday\n')
            elif day.weekday()==4:
                print(day,'is Friday\n')
            elif day.weekday()==5:
                print(day,'is Saturday\n')
            elif day.weekday()==6:
                print(day,'is Sunday\n')
               
    is_weekend(day)

##input('<Enter to exit>')
