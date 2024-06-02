def switch_to_signup(login_window, signup_window):
    login_window.withdraw()
    signup_window.deiconify()

def back_to_login(signup_window, login_window):
    signup_window.withdraw()
    login_window.deiconify()
