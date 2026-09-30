import turtle

def draw_polygon(sides):
    titi = turtle.Turtle()
    angle = 360 / sides

    for i in range(sides):
        titi.forward(100)
        titi.right(angle)



# draw_polygon(3)
# draw_polygon(4)
# draw_polygon(5)
# draw_polygon(6)
# draw_polygon(7)
# draw_polygon(8)
draw_polygon(9)





