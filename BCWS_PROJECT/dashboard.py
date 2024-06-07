
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\PYTHON\IM_PROJECT\BCWS_PROJECT\assets_dashboard\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Barangay Community Welfare System")

window.geometry("1054x792")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 792,
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
    398.0,
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
    319.0,
    87.0,
    anchor="nw",
    text="DASHBOARD",
    fill="#6A6763",
    font=("Karla ExtraBold", 66 * -1)
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

UserHelpDesk_image = PhotoImage(
    file=relative_to_assets("UserHelpDesk.png"))
UserHelpDesk = Button(
    image=UserHelpDesk_image,
    borderwidth=0,
    background= "#DED1BA",
    activebackground= "#DED1BA",
    cursor= "hand2",
    highlightthickness=0,
    command=lambda: print("UserHelpDesk clicked"),
    relief="flat"
)
UserHelpDesk.place(
    x=503.0,
    y=5.0,
    width=132.0,
    height=48.0
)

reqAssistance_image = PhotoImage(
    file=relative_to_assets("reqAssistance.png"))
reqAssistance = Button(
    image=reqAssistance_image,
    borderwidth=0,
    highlightthickness=0,
    cursor= "hand2",
    command=lambda: print("reqAssistance clicked"),
    relief="flat"
)
reqAssistance.place(
    x=119.0,
    y=189.0,
    width=367.0,
    height=250.0
)

checkStatus_image = PhotoImage(
    file=relative_to_assets("checkStatus.png"))
checkStatus = Button(
    image=checkStatus_image,
    borderwidth=0,
    highlightthickness=0,
    cursor= "hand2",
    command=lambda: print("checkStatus clicked"),
    relief="flat"
)
checkStatus.place(
    x=119.0,
    y=486.0,
    width=367.0,
    height=248.0
)

feedback_image = PhotoImage(
    file=relative_to_assets("feedback.png"))
feedback = Button(
    image=feedback_image,
    borderwidth=0,
    highlightthickness=0,
    cursor= "hand2",
    command=lambda: print("feedback clicked"),
    relief="flat"
)
feedback.place(
    x=569.0,
    y=484.0,
    width=369.0,
    height=250.0
)

programOffer_image = PhotoImage(
    file=relative_to_assets("programOffer.png"))
programOffer = Button(
    image=programOffer_image,
    borderwidth=0,
    highlightthickness=0,
    cursor= "hand2",
    command=lambda: print("programOffer clicked"),
    relief="flat"
)
programOffer.place(
    x=574.0,
    y=189.0,
    width=364.0,
    height=250.0
)
window.resizable(False, False)
window.mainloop()
