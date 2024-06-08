from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, ttk, StringVar, Frame, Radiobutton
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\PYTHON\IM_PROJECT\BCWS_PROJECT\assets_ResidentInformation\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_submit():
    if messagebox.askokcancel("Confirmation", "Please confirm that all the information you provided is accurate and true."):
        print("Form submitted")
window = Tk()
window.geometry("973x633")
window.title("Resident's Registration Form")

window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=633,
    width=973,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(527.0, 418.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(527.0, 60.0, image=image_image_2)

canvas.create_text(
    243.0,
    33.0,
    anchor="nw",
    text="REGISTRATION FORM",
    fill="#625C52",
    font=("Karla ExtraBold", 47 * -1)
)

canvas.create_text(
    33.0,
    131.0,
    anchor="nw",
    text="FULL NAME",
    fill="#000000",
    font=("Karla Bold", 25 * -1)
)

canvas.create_text(
    33.0,
    240.0,
    anchor="nw",
    text="FULL ADDRESS:",
    fill="#000000",
    font=("Karla Bold", 25 * -1)
)

canvas.create_text(
    33.0,
    342.0,
    anchor="nw",
    text="CONTACT NUMBER:",
    fill="#000000",
    font=("Karla Bold", 25 * -1)
)

canvas.create_text(
    33.0,
    450.0,
    anchor="nw",
    text="MARITAL STATUS:",
    fill="#000000",
    font=("Karla Bold", 25 * -1)
)

submit_image_1 = PhotoImage(file=relative_to_assets("submit.png"))
submit = Button(
    image=submit_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=on_submit,
    relief="flat"
)
submit.place(x=413.0, y=571.0, width=138.0, height=41.0)

canvas.create_text(
    518.0,
    450.0,
    anchor="nw",
    text="HOUSEHOLD INCOME:",
    fill="#000000",
    font=("Karla Bold", 25 * -1)
)

canvas.create_text(
    403.0,
    342.0,
    anchor="nw",
    text="GENDER:",
    fill="#000000",
    font=("Karla Bold", 25 * -1)
)

canvas.create_text(
    609.0,
    342.0,
    anchor="nw",
    text="OCCUPATION:",
    fill="#000000",
    font=("Karla Bold", 25 * -1)
)

canvas.create_text(
    33.0,
    211.0,
    anchor="nw",
    text="(e.g. Ricardo S. Dalisay)",
    fill="#3C3B38",
    font=("Karla Italic", 16 * -1)
)

canvas.create_text(
    33.0,
    421.0,
    anchor="nw",
    text="(0XXX-XXX-XXXX)",
    fill="#3C3B38",
    font=("Karla Italic", 16 * -1)
)

canvas.create_text(
    64.0,
    320.0,
    anchor="nw",
    text="House/Lot/Block No.",
    fill="#3C3B38",
    font=("Karla Italic", 16 * -1)
)

canvas.create_text(
    330.0,
    320.0,
    anchor="nw",
    text="Street",
    fill="#3C3B38",
    font=("Karla Italic", 16 * -1)
)

canvas.create_text(
    531.0,
    320.0,
    anchor="nw",
    text="Barangay",
    fill="#3C3B38",
    font=("Karla Italic", 16 * -1)
)

canvas.create_text(
    775.0,
    320.0,
    anchor="nw",
    text="City/Municipality",
    fill="#3C3B38",
    font=("Karla Italic", 16 * -1)
)

canvas.create_text(
    518.0,
    526.0,
    anchor="nw",
    text="(Estimate value)",
    fill="#3C3B38",
    font=("Karla Italic", 16 * -1)
)


canvas.create_text(
    747.0,
    211.0,
    anchor="nw",
    text="(mm-dd-yyyy)",
    fill="#3C3B38",
    font=("Karla Italic", 16 * -1)
)

canvas.create_text(
    747.0,
    131.0,
    anchor="nw",
    text="DATE OF BIRTH:",
    fill="#000000",
    font=("Karla Bold", 25 * -1)
)

fullName_image_1 = PhotoImage(file=relative_to_assets("fullName.png"))
entry_bg_1 = canvas.create_image(371.0, 188.0, image=fullName_image_1)

# Full Name
fullName = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Karla Medium", 15)
)
fullName.place(x=38.0, y=170.0, width=667.0, height=34.0)

dateBirth_image_7 = PhotoImage(file=relative_to_assets("dateBirth.png"))
entry_bg_7 = canvas.create_image(844.0, 188.0, image=dateBirth_image_7)

# Date of Birth
dateBirth = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Karla Medium", 15)
)
dateBirth.place(x=752.0, y=170.0, width=185.0, height=34.0)

fullAddress_image_2 = PhotoImage(file=relative_to_assets("fullAddress.png"))
entry_bg_2 = canvas.create_image(487.0, 297.0, image=fullAddress_image_2)

# Full Address
fullAddress = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Karla Medium", 15)
)
fullAddress.place(x=36.0, y=281.0, width=900.0, height=34.0)

contactNo_image_4 = PhotoImage(file=relative_to_assets("contactNo.png"))
entry_bg_4 = canvas.create_image(203.5, 399.0, image=contactNo_image_4)

# Contact Number
contactNo = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Karla Medium", 15)
)
contactNo.place(x=41.0, y=381.0, width=332.0, height=34.0)

occupation_image_6 = PhotoImage(file=relative_to_assets("occupation.png"))
entry_bg_6 = canvas.create_image(775.0, 399.0, image=occupation_image_6)

# Occupation
occupation = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Karla Medium", 15)
)
occupation.place(x=616.0, y=381.0, width=323.0, height=34.0)

# Gender Combobox Frame
gender_frame = Frame(window, bg="black", bd=2)
gender_frame.place(x=385, y=377, width=210, height=42)
gender = ttk.Combobox(
    gender_frame,
    state="readonly",
    values=["Male", "Female", "Prefer not to say"],
    font=("Karla Medium", 15)
)
gender.place(x=0, y=0, width=205.5, height=38)

# Household Income Combobox Frame
houseIncome_frame = Frame(window, bg="black", bd=2)
houseIncome_frame.place(x=518, y=481, width=417, height=42)
houseIncome = ttk.Combobox(
    houseIncome_frame,
    state="readonly",
    values=["None","Below Php. 10,000", "Php. 10,000 - Php. 15,000", "Php. 16,000 - Php. 20,000","Php. 21,000 - Php. 25,000", "Above Php. 25,000"],
    font=("Karla Medium", 15)
)
houseIncome.place(x=0, y=0, width=412.5, height=38)

# Marital Status
maritalStatus_var = StringVar(value="Single")

maritalStatus_single = Radiobutton(
    window,
    text="Single",
    variable=maritalStatus_var,
    value="Single",
    font=("Karla Medium", 15),
    bg="#F0EAE0",
    activebackground= "#F0EAE0"
)
maritalStatus_single.place(x=36.0, y=481.0)

maritalStatus_married = Radiobutton(
    window,
    text="Married",
    variable=maritalStatus_var,
    value="Married",
    font=("Karla Medium", 15),
    bg="#F0EAE0",
    activebackground= "#F0EAE0"
)
maritalStatus_married.place(x=150.0, y=481.0)

maritalStatus_widowed = Radiobutton(
    window,
    text="Widowed",
    variable=maritalStatus_var,
    value="Widowed",
    font=("Karla Medium", 15),
    bg="#F0EAE0",
    activebackground= "#F0EAE0"
)
maritalStatus_widowed.place(x=260.0, y=481.0)

maritalStatus_separated = Radiobutton(
    window,
    text="Separated",
    variable=maritalStatus_var,
    value="Separated",
    font=("Karla Medium", 15),
    bg="#F0EAE0",
    activebackground= "#F0EAE0"
)
maritalStatus_separated.place(x=370.0, y=481.0)

window.resizable(False, False)
window.mainloop()
