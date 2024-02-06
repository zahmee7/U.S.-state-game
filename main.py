import turtle
import pandas

scr = turtle.Screen()
scr.title("U.S. state game")
image = "blank_states_img.gif"
scr.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
gusees = []

while len(gusees) < 50:
    user_answer = scr.textinput(title=f"{len(gusees)}/50 States Correct", prompt="What's another state's name?").title()

    if user_answer in all_states:
        gusees.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_date = data[data.state == user_answer]
        t.goto(int(state_date.x), int(state_date.y))
        t.write(state_date.state.item())

    if user_answer =="Exit":
        missing = [state for state in all_states if state not in gusees]
        new_data = pandas.DataFrame(all_states)
        new_data.to_csv("leaqarn more.csv")

        break
