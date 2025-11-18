#Dictionary
my_info = {
    'Name': 'Jonathan Deuel Levardo',
    'Age': '19',
    'Hometown': 'Al Majaz 2'
    }

print(my_info['Name'])
print(my_info['Age'])
print(my_info['Hometown'])

#For Advanced Requirements
my_info['Name'] = input("What's your name? ")
my_info['Age'] = input("What's your age? ")
my_info['Hometown'] = input("Where's your hometown? ")

print(f'Your name is {my_info['Name']}')
print(f'Your age is {my_info['Age']}')
print(f'Your hometwon is {my_info['Hometown']}')

#Print Out Updated Dictionary
print(my_info)
