#Name List
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Variables
search = input('Enter name: ')
result = search in names
position = names.index(search)

#Application of User Input
if result == True:
    print(f'{search} is in the list (position: {position})')
else:
    print(f'{search} is not in the list')
