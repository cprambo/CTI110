#Charles Rambo
#04/08/2024
#P4HW2
#Creating a pay statement including hours worked, overtime hours and pay
#Using a while loop to diplay information from multiple entries until terminated by user input
'''
While (loop) employee name != "Done"
     Get payrate
     Get hours worked
     *calc ot pay, regular pay*
     add 1 to num_employees (create variable outside loop before it happens)
        num_emp=0
     total_ot += total_ot
     total_reg += reg_pay
# break
display
    num-employees
    total_ot
    total_reg {total_gross_pay
* create variables
    total_ot = 0
    total_reg = 0
'''
#Get employee name
#Get pay rate + hours worked
#Calculate overtime pay and regular pay. Store these values in variables
#Repeat until employee name is "Done"
#Display overtime total, regular pay total, gross pay total and number of employees entered

num_employees = 0
total_ot = 0.0
total_reg = 0.0
total_gross = 0.0

name = ''
while name != 'Done':
    name = input('Enter empoyee\'s name or "Done" to terminate: ')
    if name == 'Done':
        break

    num_employees = num_employees + 1
    
    hours_worked = float(input(f"How many hours did {name} work? "))
    
    pay_rate = float(input(f"What is {name}'s pay rate? "))
    
    #overtime
    if hours_worked > 40:
        overtime = hours_worked - 40
    else:
        overtime = 0

    #overtime pay
    overtime_pay = overtime * pay_rate * 1.5
    total_ot = total_ot + overtime_pay

    #regular pay
    if hours_worked > 40:
        regular_pay = pay_rate *40
    else:
        regular_pay = pay_rate * hours_worked
    total_reg = total_reg + regular_pay
    
    #gross pay
    gross_pay = regular_pay + overtime_pay
    total_gross = total_gross + gross_pay
    
    print()
    print(f'Employee name: {name}')
    print()
    print('Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay')
    print('--------------------------------------------------------------------------------')
    print(f'{hours_worked:<16.2f}{pay_rate:<12.2f}{overtime:<12.2f}{overtime_pay:<16.2f}{regular_pay:<15.2f}{gross_pay:.2f}')
    print()
    print()
print()
print(f'Total number of employees entered: {num_employees}')
print(f'Total amount paid for overtime: ${total_ot:.2f}')
print(f'Total amount paid for regular hours: ${total_reg:.2f}')
print(f'Total amount paid in gross: ${total_gross:.2f}')

  
