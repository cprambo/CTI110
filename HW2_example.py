#Rambo_Charles
#Date
#Assignment
#Description
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
dest = input('Enter your destination')
gas = int(input('Enter gas: '))

#Calculate user input

expenses = gas + hotel + food

result = budget - expenses

#Show result

print('\nRemaining balance: ' + str(result)) 
