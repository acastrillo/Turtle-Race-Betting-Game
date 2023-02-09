from turtle import Turtle, Screen
import random

# Is the game running?
is_race_on = False

# Setup the screen
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

# Create some variables to use to create the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_starting_points = [125, 75, 25, -25, -75, -125]
x_starting_point = -240
all_turtles = []


# Iterate through the number of colors, and start setting up some turtles
for t_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[t_index])
    new_turtle.goto(x=x_starting_point, y=y_starting_points[t_index])
    all_turtles.append(new_turtle)

#If there's no bet, there's no game! So if they skip, then no game.
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You win!")
            else:
                print("You've lost...")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
    

screen.exitonclick()
