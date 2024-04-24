#Chares Rambo
#03/31/2024
#CTI-110
#P4HW1 - Interacting with lists and loops with branching

'''
Create empty list of grades
Prompt user for number of grades to enter
Loop until number of grades matches user input
    Prompt for grade
    Validate grade
    Display error or append inputed grade to list of grades
Determine and print min grade
Remove min grade from grade list
Print modified list
Print Average of Grades
Print letter grade for average
'''

#List containing grades
grades = []
#User input for module grades
num_scores = int(input('How many scores do you want to enter? '))
print()
while len(grades) < num_scores:
    grade = float(input(f'Enter score #{len(grades) + 1}: '))
    if grade < 0 or grade > 100:
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
    else:
        grades.append(grade)
print()

print('------------Results------------')
print()
grade_min = min(grades)
print(f'Lowest Score: {grade_min:.2f}')
grades.pop(grades.index(grade_min))
print()
print(f'Modified List: {grades}')
print()
grade_avg = sum(grades) / len(grades)
print(f'Scores Average: {grade_avg:.2f}')
print()
if grade_avg >= 90:
    print('Grade: A')
elif grade_avg >= 80:
    print('Grade: B')
elif grade_avg >= 70:
    print('Grade: C')
elif grade_avg >= 60:
    print('Grade: D')
else:
    print('Grade: F')
print('-------------------------------')
