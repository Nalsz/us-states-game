import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 Guessed States",
                              prompt="What's another state's name").title()
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states")
        break
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_row = data[data.state == answer]
        t.goto(int(answer_row.x), int(answer_row.y))
        t.write(answer)



# screen.exitonclick()