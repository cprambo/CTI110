#Charles Rambo
#03/28/2024
#P4LAB1
#Using Turtle Graphics, Loops 



import turtle
win = turtle.Screen()
timmy = turtle.Turtle()

#add some display options
timmy.pensize(4)        #increase pen size (integer)
timmy.pencolor("purple")    #set pencolor (string)
timmy.shape("turtle")

for item in range(4):
    #Actions to happen
    timmy.forward(350)
    timmy.left(90)

for item in range(3):
    timmy.forward(350)
    timmy.left(120)
