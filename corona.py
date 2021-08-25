import turtle
import os

a = 0
b = 0    

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=1.0, height=1.0)

shape = turtle.Shape('compound')

turtle.speed(0)
turtle.pencolor("green")
turtle.penup()
turtle.goto(0,200)
turtle.pendown()

turtle.begin_poly()
while True:
    turtle.forward(a)
    turtle.right(b)

    a+=3
    b+=1

    if b==210:
        break
turtle.end_poly()

shape.addcomponent(turtle.get_poly(), 'black',"red")
screen.register_shape('corona', shape)

turtle.reset()
turtle.penup()

turtle.shape('corona')

while True:
    for theta in range(0,360):
        turtle.setheading(theta)

screen.mainloop()