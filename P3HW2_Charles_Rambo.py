#Charles Rambo
#03/24/2024
#P3HW2
#Creating a pay statement including hours worked, overtime hours and pay

name = input("Enter empoyee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

#overtime
if hours_worked > 40:
    overtime = hours_worked - 40
else:
    overtime = 0

#overtime pay
overtime_pay = overtime * pay_rate * 1.5

#regular pay
if hours_worked > 40:
    regular_pay = pay_rate *40
else:
    regular_pay = pay_rate * hours_worked

#gross pay
gross_pay = regular_pay + overtime_pay

print('-' * 45)
print(f'Employee name: {name}')
print()
print('Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay')
print('--------------------------------------------------------------------------------')
print(f'{hours_worked:<16.2f}{pay_rate:<12.2f}{overtime:<12.2f}{overtime_pay:<16.2f}{regular_pay:<15.2f}{gross_pay:.2f}')

