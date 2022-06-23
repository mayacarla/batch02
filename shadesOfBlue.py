#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program draws: the shades of blue

import turtle

turtle.colormode(255)
m = turtle.Turtle()
m.shape("turtle")
m.backward(100)

for i in range(0, 255, 10):
    m.forward(10)
    m.pensize(i)
    m.color(0, 0, i)


