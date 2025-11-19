#Dictionary of Months and Days they Contain
months = { 
    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 30,
    '9': 31,
    '10': 30,
    '11': 31,
    '12': 30
}

#User Input
user_input = input('Input month number: ')

#Ask For Leap Year
leap_year_check = input('Is it a leap year? Yes or No? ')

if leap_year_check.lower() == 'yes':
    #Update
    months['2'] = 29

    #Check Response
    if months.get(user_input) != None:
        print(months[user_input])
    else:
        print('Invalid Number!')

elif leap_year_check.lower() == 'no':
    #Check Response
    if months.get(user_input) != None:
        print(months[user_input])
    else:
        print('Invalid Number!')
else:
    print('Invalid Response!')
