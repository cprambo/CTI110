#Rambo_Charles

#03-02-2024

#P2HW1

#Travel expenses and budget

'''

Pseudocode:

Get budget (int)

Get destination (str)

Get fuel (int)

Get hotel (int)

Get food (int)

Add expenses 

Budget - expenses

Display results

'''

print('This program calculates and displays travel expenses')
print()


#get budget from user


budget = float(input('Enter budget: '))

dest = input('Enter your travel destination: ')

gas = float(input('How much do you think you will spend on gas? '))

hotel = float(input('Approximately, how much will you need for accomodation/hotel? '))

food = float(input('Last, how much do you need for food? '))

print(f"""
------------Travel Expenses------------
Location:           {dest}
Initial Budget:     ${budget: >7.2f}
Fuel:               ${gas: >7.2f}
Accomodation:       ${hotel: >7.2f}
Food:               ${food: >7.2f}
---------------------------------------""")
'''
print(f"""
------------Travel Expenses------------
Location:           {dest}
Initial Budget:     ${budget:.2f}
Fuel:               ${gas:.2f}
Accomodation:       ${hotel:.2f}
Food:               ${food:.2f}
---------------------------------------""")

print()
print('------------Travel Expenses------------')
print(f'Location:           {dest}')
print(f'Initial Budget:     ${budget:.2f}')
print(f'Fuel:               ${gas:.2f}')
print(f'Accomodation:       ${hotel:.2f}')
print(f'Food:               ${food:.2f}')
print('---------------------------------------')

'''
#Calculate user input

expenses = gas + hotel + food

result = budget - expenses

#Show result

print(f'\nRemaining balance: ${result:.2f}') 
