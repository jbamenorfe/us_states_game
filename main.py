"""This program uses Python's turtle and pandas modules to produce a program that allows the user to guess the names of states. If the user's guessed state name is correct, the name appears on its appropriate location on the map. The program then asks the user to enter another states name until he/she gets it wrong. The user sees his/her scores in real time."""

# Import necessary modules
import turtle
import pandas

# Define a method to create state_turtle
def create_state_turtle(state_name, x_pos, y_pos):
    turtle_name = turtle.Turtle()
    turtle_name.penup()
    turtle_name.hideturtle()
    turtle_name.goto(x_pos, y_pos)
    turtle_name.write(arg=state_name)
    return turtle_name

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
# screen.setup(width=800, height=600)

# Declare an image variable to hold the image file
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the states data
states = pandas.read_csv("./50_states.csv")

# Create a list of states from the state column in the states pandas object
states_list = states.state.to_list()
print(states_list)

game_is_on = True
correct_answer = 0
total_states = len(states.state)
listed_states = []
while game_is_on:
    # Take an input from the user
    answer_state = screen.textinput(title="Guess the State", prompt=f"{correct_answer}/{total_states}: What's another state's name ?")
    answer_state = answer_state.title()

    if answer_state in states_list:
        if not answer_state in listed_states:                   # Ensure that a state is not repeated
            found_state = states[states.state == answer_state]  # Get the state name and corresponding x, y coordinates
            found_state_x = int(found_state.x.iloc[0])      # Get the state's x_coordinate and convert it to an integer using the int(ser.iloc[0]) function.
            found_state_y = int(found_state.y.iloc[0])      # Get the state's y_coordinate and convert it to an integer

            # Create a turtle object for the found state
            create_state_turtle(state_name=answer_state, x_pos=found_state_x, y_pos=found_state_y)
            correct_answer += 1
            listed_states.append(answer_state)
    if correct_answer == total_states:
        screen.textinput(title="Congratulations!", prompt="You have completed the game successfully!\nPlease click on \"OK\" to close the game")
        game_is_on = False
screen.exitonclick()