# import this --> pip install tkcalendar

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import date

def submit_feedback():
    feedback_date = cal.get_date()
    feedback_text = feedback_textbox.get("1.0", tk.END).strip()
    
    # Print statements for debugging (replace with database insert logic)
    print("Feedback Date:", feedback_date)
    print("Feedback Text:", feedback_text)
    
    # Example of where to use these variables for database insertion:
    # db.insert_feedback(feedback_date, feedback_text)

# Main window
window = tk.Tk()
window.geometry("400x550")
window.configure(bg="#F0EAE0")

# Feedback Date Label
feedback_date_label = tk.Label(
    window,
    text="Feedback Date:",
    font=("Karla Bold", 18),
    bg="#F0EAE0",
    fg="#6A6763"
)
feedback_date_label.place(
    x=30,
    y=20
)

# Calendar widget
cal = Calendar(
    window,
    selectmode="day",
    year=date.today().year,
    month=date.today().month,
    day=date.today().day,
    date_pattern='mm-dd-yyyy'  # Set the date format
)
cal.place(
    x=50,  
    y=60,
    width=300,
    height=200
)

# Feedback Label
feedback_label = tk.Label(
    window,
    text="Feedback:",
    font=("Karla Bold", 18),
    bg="#F0EAE0",
    fg="#6A6763"
)
feedback_label.place(
    x=30,
    y=270
)

# Feedback Textbox 
feedback_textbox = tk.Text(
    window,
    bd=1,  
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=1,
    highlightbackground="black",  
    font=("Karla Medium", 12),
    wrap=tk.WORD
)
feedback_textbox.place(
    x=30,
    y=310,
    width=340,
    height=150  
)

# Submit button
submit_button = tk.Button(
    window,
    text="Submit",
    font=("Karla Bold", 12),
    bg="#C8B28E",
    fg="#000000",
    command=submit_feedback
)
submit_button.place(
    x=150,
    y=480,
    width=100,
    height=40
)

window.resizable(False, False)
window.mainloop()
