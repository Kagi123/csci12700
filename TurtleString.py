#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: March 09, 2022
#TurtleString

import turtle
wn = turtle.Screen()

thomasH = turtle.Turtle()

control = input("enters a string: ")

for i in control:
  if (i == 'F'):
    thomasH.forward(50)
  elif(i== 'L'):
    thomasH.left(90)
  elif(i== 'R'):
    thomasH.right(90)
  elif(i== '^'):
    thomasH.penup()
  elif(i== 'v'):
    thomasH.pendown()
  elif(i== 'B'):
    thomasH.backward(50)
  elif(i== 'S'):
    thomasH.stamp()
  elif(i== 'l'):
    thomasH.left(45)
  elif(i== 'r'):
    thomasH.right(45)
  elif(i== 'p'):
    thomasH.fillcolor('purple')
  
wn.exitonclick()
