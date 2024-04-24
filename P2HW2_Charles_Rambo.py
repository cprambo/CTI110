#Chares Rambo
#CTI-110
#P2HW2 - Interacting with lists

#List containing grades

grades = []

#User input for module grades
print('Input grades for modules 1-6')
print()
mod_1 = float(input('Enter grade for module 1: '))
mod_2 = float(input('Enter grade for module 2: '))
mod_3 = float(input('Enter grade for module 3: '))
mod_4 = float(input('Enter grade for module 4: '))
mod_5 = float(input('Enter grade for module 5: '))
mod_6 = float(input('Enter grade for module 6: '))
print()
#adding the grades to the list

grades.append(mod_1)
grades.append(mod_2)
grades.append(mod_3)
grades.append(mod_4)
grades.append(mod_5)
grades.append(mod_6)

print('------------Results------------')
print()
grade_min = min(grades)
print(f'The lowest grade is: {grade_min:.2f}')
print()
grade_max = max(grades)
print(f'The highest grade is: {grade_max:.2f}')
print()
grade_sum = sum(grades)
print(f'The sum of the grades is: {grade_sum:.2f}')
print()
grade_avg = sum(grades) / 6
print(f'The average of the grades is: {grade_avg:.2f}')
print()
print('-------------------------------')


