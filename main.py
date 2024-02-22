from turtle import Turtle, Screen
from random import randint

offset = 30
x, y = (-230, 100)
is_race_on = False
race_ = []
colors = ["red", "green", "orange", "yellow", "blue", "purple"]

screen = Screen()

screen.setup(width=500, height=400, startx=offset, starty=offset)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

def create_turtles():
    turtles = [Turtle(shape="turtle") for _ in range(6)]
    return turtles

def create_starting_line(turtles):
    global x, y
    for index, turtle in enumerate(turtles):
        turtle.penup()
        turtle.color(colors[index])
        turtle.goto(x, y)
        y += -30

turtles = create_turtles()
create_starting_line(turtles=turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        print(turtle.pos()[0])
        turtle.forward(randint(0, 10))
        if turtle.xcor() >= 220:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"La tortuga {user_bet} gana.")
            else:
                print(f"La tortuga {user_bet} pierde.")
            is_race_on = False
            break

screen.exitonclick()