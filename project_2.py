# Turtle Graphics Drawing Program
# Anthony Garrett
# 9/18/2019
# Using turtle graphics to re-create the given shapes

import turtle

# setup the initial turtle window background and size
turtle.title("Welcome")
turtle.setup(900, 900)
turtle.bgcolor('#ADD8E6')
turtle.showturtle()
turtle.pensize(5)

# Drawing the solid lines with dots first
turtle.dot(25)
turtle.setheading(45)
turtle.forward(565)
turtle.dot(25)
turtle.setheading(270)
turtle.forward(800)
turtle.dot(25)
turtle.setheading(135)
turtle.forward(1130)
turtle.dot(25)
turtle.setheading(270)
turtle.forward(800)
turtle.dot(25)
turtle.setheading(45)
turtle.forward(565)

# Drawing the top dotted Line
turtle.penup()
turtle.hideturtle()
turtle.goto(400, 400)
turtle.showturtle()
turtle.pendown()
turtle.setheading(180)
turtle.forward(100)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(150)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(150)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(100)

# Drawing the bottom dotted Line
turtle.penup()
turtle.hideturtle()
turtle.goto(400, -400)
turtle.showturtle()
turtle.pendown()
turtle.setheading(180)
turtle.forward(100)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(150)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(150)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(100)


# Used to keep the window open after the drawing is complete
turtle.mainloop()
