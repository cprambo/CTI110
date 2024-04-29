#Charles Rambo
#04/25/2024
#P5HW
#Math Quiz 

import random


def adding():
    
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print(f' {num1:>4}')
    print(f'+{num2:>4}')
    print()
    print('Enter Answer:')
    
    answer = int(input())
    numguess = 1
    while answer != num1 + num2:
        if answer > num1 + num2:
            print('Sorry answer is too high')
            
        elif answer < num1 + num2:
            print('Sorry answer is too low')
        print()
        print('Try Again: ', end = '')
        answer = int(input())
        numguess += 1
    print('Congratulations your answer is correct!')
    print(f'Number of guesses: {numguess}')
        
def subtracting():
    
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print(f' {num1:>4}')
    print(f'-{num2:>4}')
    print()
    print('Enter Answer:')
    
    answer = int(input())
    numguess = 1
    while answer != num1 - num2:
        if answer > num1 - num2:
            print('Sorry answer is too high')
            
        elif answer < num1 - num2:
            print('Sorry answer is too low')
        print()
        print('Try Again: ', end = '')
        answer = int(input())
        numguess += 1
    print('Congratulations your answer is correct!')
    print(f'Number of guesses: {numguess}')
    
    
print('Welcome to Math Quiz')
done = False
while not done:
    print()
    print('Main Menu')
    print('--------------------------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print()
    choice = input('Please choose one of the menu options: ')
    if choice == '1':
        adding()
    elif choice == '2':
        subtracting()
    elif choice == '3':
        done = True
        print('Thank you for playing...')
        print('Bye!!')
    else:
        print('Please choose an option included in the menu.')


   
    
    

