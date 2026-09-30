
import turtle
import math

def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

def sierpinski(order, size, t):
    if order == 0:
        draw_triangle(t, size)
    else:
        sierpinski(order - 1, size / 2, t)

        t.forward(size / 2)
        sierpinski(order - 1, size / 2, t)

        t.backward(size / 2)
        t.left(60)

        t.forward(size / 2)
        t.right(60)
        sierpinski(order - 1, size / 2, t)

        t.left(60)
        t.backward(size / 2)
        t.right(60)


t = turtle.Turtle()
t.speed(0) 
t.color("black") 

size = 600
height = (math.sqrt(3) / 2) * size

t.goto(-height/2, -size/2)
t.setheading(30)

sierpinski(6, size, t)
