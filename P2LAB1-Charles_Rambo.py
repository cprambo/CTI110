#Charles Rambo
#2/28/2024
#P2LAB1 - Math expressions and f-string
'''
Pseudo Code
Get mpg
Get cost of gas
(floats)
Calculate the cost to drive:
20 miles
75 miles
500 miles
Output cost to drive (7-9)

#Calulation
miles/mpg * cost of gas
'''

#get info from user
mpg = float(input("Enter the car's mpg: "))
cost = float(input("Enter the cost for a gallon of gas: "))
print ()
#Calculate the cost to drive 20,75 and 500 miles
miles_20 = (20/mpg) * cost
miles_75 =  (75/mpg) * cost
miles_500 =  (500/mpg) * cost

#output information to user
print(f"The cost to drive 20 miles is ${miles_20:.2f}\n")
print(f"The cost to drive 75 miles is ${miles_75:.2f}\n")
print(f"The cost to drive 500 miles is ${miles_500:.2f}")

