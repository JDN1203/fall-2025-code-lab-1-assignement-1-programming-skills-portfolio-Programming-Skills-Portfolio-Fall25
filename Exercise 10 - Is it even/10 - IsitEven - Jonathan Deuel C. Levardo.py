def main():
    num = int(input('Enter number: '))
    even_or_odd(num)

def even_or_odd(num):
    if num in range(0,100000,2):
        print(f'{num} is even.')
    else:
        print(f'{num} is odd.')

main()
