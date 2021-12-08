import turtle
import pandas as pd
import string

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
state_df = pd.read_csv('50_states.csv')
game_is_on = True
nr_right_guesses = 0
guesses_states_list = []
while game_is_on:
    a_state = screen.textinput(title=f'Guesses {nr_right_guesses}/50', prompt='Enter a U.S. state name:').lower()
    a_state = string.capwords(a_state, sep=None)
    state_row_df = state_df[state_df['state'] == a_state]
    # Check if state exist in dataframe.
    if not state_row_df.empty:
        a_state_name = state_row_df.iloc[0, 0]
        a_state_x = state_row_df.iloc[0, 1]
        a_state_y = state_row_df.iloc[0, 2]
        if a_state_name not in guesses_states_list:
            # Write the name of the state in the image.
            a_turtle = turtle.Turtle()
            a_turtle.penup()
            a_turtle.hideturtle()
            a_turtle.goto(a_state_x, a_state_y)
            a_turtle.write(a_state_name)
            # Increase the number of right guesses.
            nr_right_guesses += 1
            # Add the state to a list of guessed states.
            guesses_states_list.append(a_state_name)
        if nr_right_guesses == 50:
            game_is_on = False
screen.exitonclick()

# This piece of code gets the coordinates on the screen.
# def get_mouse_click(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
