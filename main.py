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
# print(states_list)

correct_answer = 0
total_states = 50
correct_states = []
correct_states_count = len(correct_states)

# all_missing_states = {}     # Dictionary to hold missing states' name, x-cor and y-cor
# missing_state_list = []     # List to hold missing state names
# missing_states_xcor_list = []   # List to hold missing state's x-coordinates
# missing_states_ycor_list = []   # List to hold missing state's y-coordinates


while correct_states_count < total_states:
    # Take an input from the user
    answer_state = screen.textinput(title=f"{correct_answer}/{total_states} States Correct", prompt= "What's another state's name ?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []
        for state_item in states_list:
            if not state_item in correct_states:
                missing_states.append(state_item)
                # missing_state = states[states.state == state_item]  # Missing state (row object)

                # missing_state_item = missing_state.state.item()     # Missing state's name
                # xcor = missing_state.x.item()                       # Missing state's x-coordinate
                # ycor = missing_state.y.item()                       # Missing state's y-coordinate
                #
                # missing_state_list.append(missing_state_item)       # Add missing state's name to missing state list
                # missing_states_xcor_list.append(xcor)               # Add missing state's xcor to its list
                # missing_states_ycor_list.append(ycor)               # Add missing state's ycor to its list
                #
                # # Populate the dictionary of all missing states
                # all_missing_states = {
                #     "state": missing_state_list,
                #     "x": missing_states_xcor_list,
                #     "y": missing_states_ycor_list
        # }
        #
        # # Convert all_missing_state dictionary to pandas dataframe
        # df = pandas.DataFrame(all_missing_states)

        # Store df in a .csv file
        # df.to_csv("missing_states.csv")
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        if not answer_state in correct_states:                   # Ensure that a state is not repeated
            found_state = states[states.state == answer_state]  # Get the state name and corresponding x, y coordinates
            found_state_x = int(found_state.x.iloc[0])      # Get the state's x_coordinate and convert it to an integer using the int(ser.iloc[0]) function.
            found_state_y = int(found_state.y.iloc[0])      # Get the state's y_coordinate and convert it to an integer

            # Create a turtle object for the found state
            create_state_turtle(state_name=answer_state, x_pos=found_state_x, y_pos=found_state_y)
            correct_answer += 1
            correct_states.append(answer_state)