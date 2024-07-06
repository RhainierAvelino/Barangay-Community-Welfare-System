from pathlib import Path
import subprocess
import sys
import tkinter as tk

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\PYTHON\IM_PROJECT\BCWS_PROJECT\assets_sign_up\frame0")


#To hide the entry in password 
def toggle_entry_visibility(event):
    if event.widget == sign_up_entry_1:
        sign_up_entry_1.config(show='*')
        sign_up_entry_2.config(shouw='*')
    elif event.widget == sign_up_entry_2:
        sign_up_entry_1.config(show='*')
        sign_up_entry_2.config(show='*')

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Close the Sign_up.py and open Login.py
def open_login():
    window.destroy()
    subprocess.Popen(["python", "c:/Users/User/Desktop/PYTHON/IM_PROJECT/BCWS_PROJECT/Login.py"])

window = Tk()

window.geometry("541x792")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=792,
    width=541,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("sign_up_image_1.png"))
image_1 = canvas.create_image(
    270.0,
    398.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("sign_up_image_2.png"))
image_2 = canvas.create_image(
    270.0,
    20.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("sign_up_image_3.png"))
image_3 = canvas.create_image(
    280.38050079345703,
    436.4579162597656,
    image=image_image_3
)

#sign_up_entry_1 is for the Password
entry_image_1 = PhotoImage(
    file=relative_to_assets("sign_up_entry_1.png"))
entry_bg_1 = canvas.create_image(
    269.026611328125,
    430.4468059539795,
    image=entry_image_1
)
sign_up_entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show='*',
    font=("Karla Medium", 19)
)
sign_up_entry_1.place(
    x=69.0,
    y=403.0,
    width=400.05322265625,
    height=52.893611907958984
)
sign_up_entry_1.bind("<FocusOut>", toggle_entry_visibility)

image_image_4 = PhotoImage(
    file=relative_to_assets("sign_up_image_4.png"))
image_4 = canvas.create_image(
    280.38050079345703,
    546.4578857421875,
    image=image_image_4
)

#sign_up_entry_2 is for the Confirm Password
entry_image_2 = PhotoImage(
    file=relative_to_assets("sign_up_entry_2.png"))
entry_bg_2 = canvas.create_image(
    269.026611328125,
    540.4468059539795,
    image=entry_image_2
)
sign_up_entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show='*',
    font=("Karla Medium", 19)
)
sign_up_entry_2.place(
    x=69.0,
    y=513.0,
    width=400.05322265625,
    height=52.893611907958984
)
sign_up_entry_2.bind("<FocusOut>", toggle_entry_visibility)

canvas.create_text(
    57.0,
    475.0,
    anchor="nw",
    text="Confirm password",
    fill="#000000",
    font=("Karla Bold", 23 * -1)
)

canvas.create_text(
    54.0,
    363.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Karla Bold", 23 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("sign_up_image_5.png"))
image_5 = canvas.create_image(
    276.38050079345703,
    214.45791625976562,
    image=image_image_5
)

#sign_up_entry_3 is for Username
entry_image_3 = PhotoImage(
    file=relative_to_assets("sign_up_entry_3.png"))
entry_bg_3 = canvas.create_image(
    265.026611328125,
    208.4468059539795,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Karla Medium", 19)
)
entry_3.place(
    x=65.0,
    y=181.0,
    width=400.05322265625,
    height=52.893611907958984
)

image_image_6 = PhotoImage(
    file=relative_to_assets("sign_up_image_6.png"))
image_6 = canvas.create_image(
    276.38050079345703,
    324.4578857421875,
    image=image_image_6
)

#sign_up_entry_3 is for Email
entry_image_4 = PhotoImage(
    file=relative_to_assets("sign_up_entry_4.png"))
entry_bg_4 = canvas.create_image(
    265.026611328125,
    318.4468059539795,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Karla Medium", 19)
)
entry_4.place(
    x=65.0,
    y=291.0,
    width=400.05322265625,
    height=52.893611907958984
)

canvas.create_text(
    53.0,
    253.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("Karla Bold", 23 * -1)
)

canvas.create_text(
    50.0,
    141.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Karla Bold", 23 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("sign_up_image_7.png"))
image_7 = canvas.create_image(
    35.0,
    20.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("sign_up_image_8.png"))
image_8 = canvas.create_image(
    67.0,
    20.0,
    image=image_image_8
)

button_image_1 = PhotoImage(
    file=relative_to_assets("sign_up_button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    cursor= "hand2",
    command=lambda: print("sign_up_button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=130.0,
    y=593.0,
    width=282.0,
    height=96.0
)

#sign_up_button_2 is for going back to Login
button_image_2 = PhotoImage(
    file=relative_to_assets("sign_up_button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    cursor= "hand2",
    command=open_login,
    relief="flat"
)
button_2.place(
    x=119.0,
    y=699.0,
    width=311.0,
    height=71.0
)

image_image_9 = PhotoImage(
    file=relative_to_assets("sign_up_image_9.png"))
image_9 = canvas.create_image(
    269.0,
    97.0,
    image=image_image_9
)
window.resizable(True, True)
window.mainloop()
