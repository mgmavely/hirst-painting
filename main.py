import colorgram
import turtle as t
import random

colors = colorgram.extract('image.jpg', 30)

T = t.Turtle()
T.speed("fastest")
S = t.Screen()
S.colormode(255)
T.penup()
T.setposition(-400,-300)
for j in range(-300, 300, 50):
    for i in range(-400, 400, 50):
        T.setposition(i, j)
        c = random.choice(colors).rgb
        T.color(c.r, c.g, c.b)
        T.dot(20)

S.exitonclick()