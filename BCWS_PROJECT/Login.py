
#try if mag change

from pathlib import Path
import subprocess
import sys

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\PYTHON\IM_PROJECT\BCWS_PROJECT\assets_login\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Close the Login.py and open Sign_up.py

def open_sign_up():
    window.destroy()
    subprocess.Popen(["python", "c:/Users/User/Desktop/PYTHON/IM_PROJECT/BCWS_PROJECT/Sign_up.py"])

#To hide the entry in password 
def toggle_entry_visibility():
    global entry_2_hidden
    entry_2_hidden = not entry_2_hidden
    if entry_2_hidden:
        entry_2.config(show='')  # Show characters normally
    else:
        entry_2.config(show='*')  # Show asterisks for privacy

window = Tk()

window.geometry("541x792")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 792,
    width = 541,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)


# Define global variable for entry_2 visibility
entry_2_hidden = False


image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    270.0,
    398.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    270.0,
    20.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    271.0,
    256.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    278.38050079345703,
    433.4579162597656,
    image=image_image_4
)

#entry_1 is for Username
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    267.026611328125,
    427.4468059539795,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Karla Medium", 19) # Show asterisks by default

)
entry_1.place(
    x=67.0,
    y=400.0,
    width=400.05322265625,
    height=52.893611907958984
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    278.38050079345703,
    538.4578857421875,
    image=image_image_5
)
# entry_2 is the Password
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(267.026611328125, 532.4468059539795, image=entry_image_2)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show='*',
    font=("Karla Medium", 19) # Show asterisks by default
)
entry_2.place(x=67.0, y=505.0, width=400.05322265625, height=52.893611907958984)

canvas.create_text(
    55.0,
    467.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Karla Bold", 27 * -1)
)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=toggle_entry_visibility,  # Toggle visibility on button click
    relief="flat"
)
button_3.place(x=413.0, y=509.0, width=57.0, height=46.0)


canvas.create_text(
    52.0,
    360.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Karla Bold", 27 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    262.0,
    104.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    35.0,
    20.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    67.0,
    20.0,
    image=image_image_8
)

#button_1 for login
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=123.0,
    y=593.0,
    width=290.0,
    height=91.0
)


#button_2 is to create an account (will go in Sign up)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_sign_up,
    relief="flat"
)
button_2.place(
    x=97.0,
    y=694.0,
    width=327.0,
    height=70.0
)

#button_3 is used to hide and unhide the password
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=toggle_entry_visibility,  # Toggle visibility on button click
    relief="flat"
)
button_3.place(x=413.0, y=509.0, width=57.0, height=46.0)
window.resizable(False, False)
window.mainloop()
