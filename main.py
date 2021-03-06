from turtle import Turtle, Screen
import pandas as pd
FONT = ("courier", 10, "normal")
# setting up the screen
screen = Screen()
screen.title("U.S. States Game")
# setting the gif as the new shape for the turtle
image = "blank_states_img.gif"
screen.addshape(image)
screen_turtle = Turtle()
screen_turtle.shape(image)

tim = Turtle()
tim.penup()
tim.hideturtle()
# reading the csv file using pandas
data = pd.read_csv("50_states.csv")
states_list = data.state.to_list()
user_guess_list = []
while len(user_guess_list) < 50:
    user_input = screen.textinput(title=f"{len(user_guess_list)}/50 States Correct",
                                  prompt="What's another state name?").title()
    if user_input == "Exit":
        break
    elif user_input in user_guess_list:
        pass
    elif user_input in states_list:
        current_state = data[data["state"] == user_input]
        x = int(current_state["x"])
        y = int(current_state["y"])
        tim.goto(x, y)
        tim.write(user_input, move=False, align="center", font=FONT)
        user_guess_list.append(user_input)
missing_states = []
for state in states_list:
    if state not in user_guess_list:
        missing_states.append(state)
states_to_learn = {
    "states": missing_states
}

new_data = pd.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")
