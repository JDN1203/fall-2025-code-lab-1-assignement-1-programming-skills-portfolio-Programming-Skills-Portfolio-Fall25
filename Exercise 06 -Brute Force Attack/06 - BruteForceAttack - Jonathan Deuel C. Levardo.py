attempts = 5
password = '12345'

while attempts > 0:
    guess = input('Enter password (5 Digits): ')
    if guess == password:
        print('Access Granted')
        break

    else:
        attempts -= 1
        print('Try Again!')

    if attempts == 0:
        print('You have exceeded your chances! The authorities have been notified.')
