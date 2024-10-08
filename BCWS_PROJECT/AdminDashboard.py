
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\PYTHON\IM_PROJECT\BCWS_PROJECT\assets_AdminDashboard\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Barangay Community Welfare System")
window.geometry("1054x829")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 829,
    width = 1054,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    527.0,
    415.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    527.0,
    29.0,
    image=image_image_2
)

canvas.create_text(
    154.0,
    84.0,
    anchor="nw",
    text="ADMIN DASHBOARD",
    fill="#6A6763",
    font=("Karla ExtraBold", 75 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    39.0,
    28.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    80.0,
    28.0,
    image=image_image_4
)

helpDesk_image = PhotoImage(
    file=relative_to_assets("helpDesk.png"))
helpDesk = Button(
    image=helpDesk_image,
    borderwidth=0,
    highlightthickness=0,
    cursor= "hand2",
    command=lambda: print("helpDesk clicked"),
    relief="flat"
)
helpDesk.place(
    x=722.0,
    y=535.0,
    width=275.0,
    height=253.0
)

feedbackManagement_image = PhotoImage(
    file=relative_to_assets("feedbackManagement.png"))
feedbackManagement = Button(
    image=feedbackManagement_image,
    borderwidth=0,
    highlightthickness=0,
    cursor= "hand2",
    command=lambda: print("feedbackManagement clicked"),
    relief="flat"
)
feedbackManagement.place(
    x=720.0,
    y=190.0,
    width=275.0,
    height=253.0
)

AssReqManagement_image = PhotoImage(
    file=relative_to_assets("AssReqManagement.png"))
AssReqManagement = Button(
    image=AssReqManagement_image,
    borderwidth=0,
    highlightthickness=0,
    cursor= "hand2",
    command=lambda: print("AssReqManagement clicked"),
    relief="flat"
)
AssReqManagement.place(
    x=389.0,
    y=400.0,
    width=275.0,
    height=253.0
)

ResidentManagement_image = PhotoImage(
    file=relative_to_assets("ResidentManagement.png"))
ResidentManagement = Button(
    image=ResidentManagement_image,
    borderwidth=0,
    highlightthickness=0,
    cursor= "hand2",
    command=lambda: print("ResidentManagement clicked"),
    relief="flat"
)
ResidentManagement.place(
    x=55.0,
    y=188.0,
    width=277.0,
    height=256.0
)

ProgramManagement_image = PhotoImage(
    file=relative_to_assets("ProgramManagement.png"))
ProgramManagement = Button(
    image=ProgramManagement_image,
    borderwidth=0,
    highlightthickness=0,
    cursor= "hand2",
    command=lambda: print("ProgramManagement clicked"),
    relief="flat"
)
ProgramManagement.place(
    x=57.0,
    y=535.0,
    width=275.0,
    height=253.0
)

logout_image = PhotoImage(
    file=relative_to_assets("logout.png"))
logout = Button(
    image=logout_image,
    borderwidth=0,
    background= "#DED1BA",
    activebackground= "#DED1BA",
    cursor= "hand2",
    highlightthickness=0,
    command=lambda: print("logout clicked"),
    relief="flat"
)
logout.place(
    x=906.0,
    y=5.0,
    width=132.0,
    height=48.0
)
window.resizable(False, False)
window.mainloop()
