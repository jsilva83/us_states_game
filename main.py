import turtle
import pandas as pd
import string

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
states_df = pd.read_csv('50_states.csv')
game_is_on = True
nr_right_guesses = 0
guessed_states_list = []
while game_is_on:
    # My version.
    # a_state = screen.textinput(title=f'Guesses {nr_right_guesses}/50', prompt='Enter a U.S. state name:').lower()
    # a_state = string.capwords(a_state, sep=None)
    # Alternative.
    a_state = screen.textinput(title=f'Guesses {nr_right_guesses}/50', prompt='Enter a U.S. state name:').title()
    if a_state == 'Exit':
        break
    state_row_df = states_df[states_df['state'] == a_state]
    # Check if state exist in dataframe.
    if not state_row_df.empty:
        # My version.
        # a_state_name = state_row_df.iloc[0, 0]
        # a_state_x = state_row_df.iloc[0, 1]
        # a_state_y = state_row_df.iloc[0, 2]
        # Alternative
        a_state_name = state_row_df['state'].item()
        a_state_x = state_row_df['x'].item()
        a_state_y = state_row_df['y'].item()
        if a_state_name not in guessed_states_list:
            # Write the name of the state in the image.
            a_turtle = turtle.Turtle()
            a_turtle.penup()
            a_turtle.hideturtle()
            a_turtle.goto(a_state_x, a_state_y)
            a_turtle.write(a_state_name)
            # Increase the number of right guesses.
            nr_right_guesses += 1
            # Add the state to a list of guessed states.
            guessed_states_list.append(a_state_name)
        if nr_right_guesses == 50:
            game_is_on = False
# Write the missing states to file 'states_to_learn.csv'
# Create an intersection between the guessed_states_list and the states_df dataframe
non_guessed_states_df = states_df[~states_df['state'].isin(guessed_states_list)]
non_guessed_states_sr = non_guessed_states_df['state']
non_guessed_states_sr.to_csv('states_to_learn.csv')

# This piece of code gets the coordinates on the screen.
# def get_mouse_click(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
