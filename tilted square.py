#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: February 04, 2022
#This program draws a tilted square.

import turtle
wn = turtle.Screen()

thomasH = turtle.Turtle()
for i in range(60):
    thomasH.forward(5*i)
    thomasH.left(91)

wn.exitonclick()
