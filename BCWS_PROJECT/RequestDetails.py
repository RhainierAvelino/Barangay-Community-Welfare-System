import tkinter as tk
from tkinter import ttk

def on_combobox_change(event):
    if combobox.get() == "Others":
        other_entry.config(state='normal')
    else:
        other_entry.config(state='disabled')

def submit_request():
    selected_program = combobox.get()
    other_program = other_entry.get() if selected_program == "Others" else ""
    request_details = request_details_entry.get()
    
    # Print statements for debugging (replace with database insert logic)
    print("Selected Program:", selected_program)
    print("Other Program:", other_program)
    print("Request Details:", request_details)
    
    # Example of where to use these variables for database insertion:
    # db.insert_request(selected_program, other_program, request_details)

window = tk.Tk()
window.geometry("541x300")
window.configure(bg="#F0EAE0")

# Combobox for program offers
combobox = ttk.Combobox(
    window,
    values=["Medical Kit", "School Supplies", "Relief goods", "Others"],
    font=("Karla Medium", 12),
    state="readonly"
)
combobox.place(
    x=65,
    y=40,
    width=400,
    height=30
)
combobox.bind("<<ComboboxSelected>>", on_combobox_change)

# Entry for Others 
other_entry = tk.Entry(
    bd=1, 
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=1,
    highlightbackground="black",  
    font=("Karla Medium", 12)
)
other_entry.place(
    x=65,
    y=80,
    width=400,
    height=30
)
other_entry.config(state='disabled')

# Label and textbox for Request Details 
request_details_label = tk.Label(
    window,
    text="Request Details",
    font=("Karla Bold", 12),
    bg="#F0EAE0",
    fg="#000000"
)
request_details_label.place(
    x=65,
    y=120
)

request_details_entry = tk.Entry(
    bd=1, 
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=1,
    highlightbackground="black", 
    font=("Karla Medium", 12)
)
request_details_entry.place(
    x=65,
    y=150,
    width=400,
    height=30
)

# Submit button
submit_button = tk.Button(
    window,
    text="Submit",
    font=("Karla Bold", 12),
    bg="#C8B28E",
    fg="#000000",
    cursor= "hand2",
    command=submit_request
)
submit_button.place(
    x=220,
    y=200,
    width=100,
    height=40
)

window.resizable(False, False)
window.mainloop()
