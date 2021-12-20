# import colorgram
import turtle 
import random

# colors_from_colorgram = colorgram.extract('image.jpg', 25)
# rgb_colors = []

# for i in colors_from_colorgram:
#     rgb_colors.append((i.rgb.r, i.rgb.g, i.rgb.b))

# print(rgb_colors)

turtle.colormode(255)
color_list = [(240, 226, 206), (206, 157, 100), (46, 112, 147), (123, 166, 191), (213, 227, 237), (218, 236, 228), (239, 220, 229), (196, 137, 160), (145, 70, 97), (153, 88, 54), (171, 157, 46), (50, 128, 92), (131, 179, 155), (190, 90, 119), (222, 201, 134), (202, 94, 73), (75, 159, 126), (129, 28, 49), (53, 155, 178), (226, 170, 187), (77, 25, 50), (155, 211, 193), (233, 173, 161), (107, 120, 163), (21, 48, 82)]
tim = turtle.Turtle()
tim.pensize(15)
tim.speed(0)
tim.hideturtle()

tim.penup()
tim.goto(-275,-225)
x = -275
y = -225
for i in range(1,11):
    for j in range(10):
        tim.color(random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.forward(1)
    tim.penup()
    tim.goto(x, y + 50*i)

screen = turtle.Screen()
screen.exitonclick()