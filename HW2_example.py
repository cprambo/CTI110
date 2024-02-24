#Rambo_Charles
#02-23-2024
#P1HW2
#Travel Expenses Input and Result
'''
Pseudocode:
Get budget  (int)
Get destination (str)
Get gas (int)
Get hotel (int)
Get food (int)
Add expenses 
Budget - expenses
Display results
'''
print('This program calculates and displays travel expenses')
#get budget from user

budget = int(input('Enter budget: '))
dest = input('Enter your destination: ')
gas = int(input('Enter gas: '))
hotel = int(input('Enter hotel: '))
food = int(input('Enter food: '))

#Calculate user input

expenses = gas + hotel + food

result = budget - expenses

#Show result

print('\nRemaining balance: ' + str(result)) 
