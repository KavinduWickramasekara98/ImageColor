###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random

import colorgram
import turtle as t
t.colormode(255)
dot = t.Turtle()
rgb_colors = []

colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)
for _ in range(10):
    for _ in range(10):
        dot.pendown()
        dot.pencolor(random.choice(rgb_colors))
        dot.dot(10)
        dot.penup()
        dot.forward(15)
    dot.penup()
    dot.backward(150)
    dot.left(90)
    dot.forward(15)
    dot.right(90)
    dot.pendown()

t.Screen().exitonclick()