#Charles Rambo
#2/28/2024
#P2LAB2 - Math expressions and f string


'''
get 4 floats from user
calculate product(x)
calculate average (+,/)
output w/ 0 decimal
output w/ 3 decimal
'''
#get info from user
num1 = float(input("Enter a float: "))
num2 = float(input("Enter a float: "))
num3 = float(input("Enter a float: "))
num4 = float(input("Enter a float: "))
print()

#calculate the product
product = num1 * num2 * num3 * num4

#calculate average
average = (num1 + num2 + num3 + num4) / 4

#Output variables with 0 decimal places
print(f"The product of the numbers is {product:.0f}")
print(f"The average of the numbers is {average:.0f}")
#Output variables with 3 decimal places
print()
print(f"The product of the numbers is {product:.3f}")
print(f"The average of the numbers is {average:.3f}")

