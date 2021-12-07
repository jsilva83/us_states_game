import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
state_df = pd.read_csv('50_states.csv')
game_is_on = True
nr_right_states = 0
guesses_states_list = []
while game_is_on:
    a_state = screen.textinput(title=f'Guesses {nr_right_states}/50',
                               prompt='Enter a U.S. state name:').lower().capitalize()
    state_row_df = state_df[state_df['state'] == a_state]
    if not state_row_df.empty:
        # Write the name of the state in the image.
        # Increase the number of right guesses.
        nr_right_states += 1
        # Add the state to a list of guessed states.
        guesses_states_list.append(state_row_df['state'])
    print(state_row_df)
screen.exitonclick()

# This piece of code gets the coordinates on the screen.
# def get_mouse_click(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
