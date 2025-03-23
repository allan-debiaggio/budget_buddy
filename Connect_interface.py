import customtkinter as ctk
from PIL import Image
import os
from database import ManageDatabase  # Import the ManageDatabase class
from variable_test import get_env_variable  # Import the get_env_variable function

# Theme configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main window creation
root = ctk.CTk()
root.title("Budget Buddy")
root.geometry("1366x768")
root.resizable(False, False)  # Lock window resizing

# Loading background image
background_image = Image.open("asset/screen_connect.png")
background_photo = ctk.CTkImage(light_image=background_image, dark_image=background_image, size=(1366, 768))

# Creating label for background image
background_label = ctk.CTkLabel(root, image=background_photo, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Adding title on background image
title_label = ctk.CTkLabel(root, text="Budget Buddy", font=("Arial", 42), bg_color="transparent")
title_label.place(relx=0.5, rely=0.1, anchor="center")

# Creating frame to group elements
frame = ctk.CTkFrame(root, width=360, height=414, fg_color="#4D4D4D", corner_radius=0)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Button functions definition
def validate_credentials(email, password):
    db_manager = ManageDatabase(
        host=get_env_variable("DB_HOST"),
        user=get_env_variable("DB_USER"),
        password=get_env_variable("DB_PASSWORD"),
        database=get_env_variable("DB_NAME")
    )
    db_manager.connect_database()
    query = "SELECT id_account, first_name, last_name, password FROM account WHERE email = %s"
    result = db_manager.execute_query("read", query, (email,))
    db_manager.close()
    if result:
        user_id, first_name, last_name, stored_password = result[0]
        if stored_password == password:  # Compare plain passwords
            return user_id, first_name, last_name
    return None, None, None

def on_enter_click():
    email = username_entry.get()  # Get text from email field
    password = password_entry.get()  # Get text from password field
    user_id, first_name, last_name = validate_credentials(email, password)
    if user_id:
        print(f"Email: {email}, Password: {password}")
        # Pass user ID to main_interface.py
        os.environ["USER_ID"] = str(user_id)
        root.destroy()
        os.system("python main_interface.py")  # Open main_interface.py
    else:
        error_label.configure(text="Wrong email / password")

def on_create_account_click():
    root.destroy()
    os.system("python register_interface.py")  # Open register_interface.py

# Adding UI elements to the frame

# Connect label
connect_label = ctk.CTkLabel(root, text="Connect", font=("Arial", 10), bg_color="#4D4D4D")
connect_label.place(x=665, y=203)

# Email entry field
username_entry = ctk.CTkEntry(
    root,
    width=313.04,
    height=64,
    placeholder_text="Email",
    bg_color="#4D4D4D",
    fg_color="#2C2C2C",
    corner_radius=10,
    font=("Arial", 14)
)
username_entry.place(x=527.43, y=238.4)

# Password entry field
password_entry = ctk.CTkEntry(
    root,
    width=313.04,
    height=64,
    placeholder_text="Password",
    bg_color="#4D4D4D",
    fg_color="#2C2C2C",
    corner_radius=10,
    font=("Arial", 14),
    show="*"  # Hide entered text (for passwords)
)
password_entry.place(x=527.43, y=320)

# Error message label
error_label = ctk.CTkLabel(root, text="", font=("Arial", 12), bg_color="#4D4D4D", text_color="red")
error_label.place(x=527, y=400)

# Enter button
enter_button = ctk.CTkButton(
    root,
    width=98.66,
    height=64,
    text="Enter",
    corner_radius=10,
    bg_color="#4D4D4D",
    fg_color="#2C2C2C",
    command=on_enter_click  # Link function to button
)
enter_button.place(x=741.81, y=473.6)

# Create account button
create_account_button = ctk.CTkButton(
    root,
    width=98.66,
    height=64,
    text="Create an account",
    corner_radius=10,
    bg_color="#4D4D4D",
    fg_color="#2C2C2C",
    command=on_create_account_click
)
create_account_button.place(x=527, y=474)

# Launch main interface loop
root.mainloop()