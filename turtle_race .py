
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race, enter colour")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]

all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_turtle = turtles.pencolor()
            if winning_turtle == user_bet:
                print(f"you have won! {winning_turtle} turtle is the winner")
            else:
                print(f"you have lost! {winning_turtle} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtles.forward(random_distance)
screen.exitonclick()