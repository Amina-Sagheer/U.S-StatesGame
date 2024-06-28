import turtle as t
from turtle import *
import pandas

timmy = Turtle()
my_screen = Screen()
score = 0
image = "blank_states_img.gif"
my_screen.addshape(image)
t.shape(image)
while True:
    my_screen.title(f"{score}/50 States")
    user_input = textinput(title="U.S. Sates Game", prompt="Enter the name of a US state.")
    name = user_input.title()
    names = pandas.read_csv("50_states.csv")
    if name == "Exit":
        break
    for index, row in names.iterrows():
        if row["state"] == name:
            x = row["x"]
            y = row["y"]
            score += 1
            timmy.penup()
            timmy.goto(x, y)
            timmy.write(name)
            timmy.hideturtle()
        else:
            continue

my_screen.bye()
