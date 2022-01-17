import tkinter as tk
from random import shuffle
import numpy as np


def _shuffler(num):
    """Shuffle the team and split the players into 2 or 3 teams.
    """
    group1 = []
    group2 = []
    group3 = []

    list_people = list(range(1, num+1))
    shuffle(list_people)

    if len(list_people) <= 14:
        num_group = np.array_split(list_people, 2)
        group1.extend(list(num_group[0]))
        group2.extend(list(num_group[1]))
        group3.append(None)
    elif len(list_people) > 14:
        num_group = np.array_split(list_people, 3)
        group1.extend(list(num_group[0]))
        group2.extend(list(num_group[1]))
        group3.extend(list(num_group[2]))

    if num > 18 and num <= 21:
        label["text"] = "Too many players for 3 teams but fine...\n" + \
            "Team 1 {0}\nTeam 2 {1}\nTeam 3 {2}\n".format(group1, group2, group3)
    else:
        label["text"] = "Team 1 {0}\nTeam 2 {1}\nTeam 3 {2}\n".format(group1, group2, group3)

def _main(num) -> None:
    """Read the number of players from the user and make teams.
    """
    try:
        num_int = int(num)
    except ValueError:
        label["text"] = "Please enter an integer number!"
    else:
        if num_int > 18 and num_int <= 21:
            label["text"] = "Too many players for 3 teams but fine..."
            _shuffler(num_int)
        elif num_int > 21:
            label["text"] = "Impossible to make 3 teams!\nGood luck next time, late fellows!"
        elif num_int < 0:
            label["text"] = "Negative number of players!\nhum... interesting"
        else:
            _shuffler(num_int)
    # Put the placeholder text back after making teams
    _release()

# call function when we _click on entry box
def _click(*args):
    entry.delete(0, 'end')
  
# call function when we leave shuffle button
def _release(*args):
    entry.delete(0, 'end')
    entry.insert(0, PLACEHOLDER)
    root.focus()

#################################
# The logic of the _shuffler GUI #
#################################

WIDTH = 600
HEIGHT = 500
PLACEHOLDER = 'The number of players... '

root = tk.Tk()
# Set the minimum window size
root.minsize(WIDTH, HEIGHT)

# Add a background image to fill up the root
background_image = tk.PhotoImage(file="maple_leaves_bg.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1.0)

# Add text in Entry box
entry.insert(0, PLACEHOLDER)
# Remove the placeholder text at a _click
entry.bind("<Button>", _click)

button = tk.Button(frame, text="SHUFFLE", font=40, bg="gray", fg="black", command=lambda: _main(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.65, anchor="n")

label = tk.Label(lower_frame, text="Team information", bg="black", fg="white", font=("Arial", 18), justify="left", bd=4)
label.place(relwidth=1, relheight=1)

if __name__ == "__main__":
    root = tk.mainloop()