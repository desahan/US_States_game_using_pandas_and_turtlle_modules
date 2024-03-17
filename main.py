from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)

turt = Turtle()
turt.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state
states = states.tolist()

game_is_on = True
correct_guesses = []
score = 0
while game_is_on:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    answer = answer.title()
    if answer == "Exit":
        game_is_on = False
    if answer not in correct_guesses and answer in states:
        correct_guesses.append(answer)
        score += 1
        row = data[data["state"] == answer]
        x_cor = row["x"].values[0]
        y_cor = row["y"].values[0]
        text = Turtle()
        text.penup()
        text.hideturtle()
        text.goto(x_cor, y_cor)
        text.write(f"{answer}")
        if score == 50:
            game_is_on = False

# make a csv file of missing states
missed_states = [state for state in states if state not in correct_guesses]
new_data = pandas.DataFrame(missed_states)
new_data.to_csv("states_to_learn.csv")
