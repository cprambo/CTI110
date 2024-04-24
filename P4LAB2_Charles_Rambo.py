#Charles Rambo
#03/27/2024
#P4LAB2
# Output range with increment of 5 using while loop

'''
1. Get information from the user
    2 integers
2. var1 higher than var2
    while var1 is >= var2
    display error message.
    return to start
3. var1 < var2
    show incrementing values
'''

#create variables for user input of two values as integers

var1 = int(input("Enter the smaller integer: "))
print()
var2 = int(input("Enter the larger integer: "))

#while var1 is > var2 allow user to re-enter integers

while var1 >= var2:
    print("First number must be smaller than the second. Try again")
    var1 = int(input("Enter the smaller integer: "))
    print()
    var2 = int(input("Enter the larger integer: "))
#The while loop has broken. Values were entered correctly
#output in increments of 5 from the lowest to the highest
print()
for num in range(var1, var2+1, 5):
    print(num, end = " ")
