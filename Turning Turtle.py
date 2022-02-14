#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: February 13, 2022
#For each number, turn the turtle
#left the degrees entered and then the turtle should move forward 100.

import turtle
wn = turtle.Screen()

thomasH = turtle.Turtle()
for i in range(5):
    num = input("Enter a number: ")
    thomasH.left(int(num))
    thomasH.forward(100)

wn.exitonclick()

