import customtkinter as ctk
from PIL import Image
import os
import re  # Add this import for regular expressions
from database import ManageDatabase  # Import the ManageDatabase class
from variable_test import get_env_variable  # Import the get_env_variable function

# Theme configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main window creation
root = ctk.CTk()
root.title("Budget Buddy")
root.geometry("1366x768")
root.resizable(False, False) 

# Loading background image
background_image = Image.open("asset/register_background.png")
background_photo = ctk.CTkImage(light_image=background_image, dark_image=background_image, size=(1366, 768))

# Creating label for background image
background_label = ctk.CTkLabel(root, image=background_photo, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Creating frame to group elements
frame = ctk.CTkFrame(root, width=360, height=604, fg_color="#4D4D4D", corner_radius=0)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Button functions definition
def validate_email(email):
    return "@" in email and "." in email

def validate_password(password):
    if len(password) < 10:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

# Comment out the hash_password function
# def hash_password(password):
#     """hash the password of the user with bcrypt and a pepper"""
#     # attention pour le hachage, il faut que password soit en string!!
#     pepper = get_env_variable("PEPPER")
#     peppered_password = password + pepper
#     salt = bcrypt.gensalt()
#     hashed = bcrypt.hashpw(peppered_password.encode(), salt)
#     return hashed.decode()

def on_enter_click():
    first_name = first_name_entry.get() 
    last_name = last_name_entry.get()
    email = email_entry.get() 
    password = password_entry.get() 

    if not validate_email(email) or not validate_password(password):
        error_label.configure(text="Invalid information")
    else:
        error_label.configure(text="")
        # hashed_password = hash_password(password)  # Comment out this line
        print(f"First name: {first_name}, Last name: {last_name}, Email: {email}, Password: {password}")
        
        # Insert credentials into the database
        db_manager = ManageDatabase(
            host=get_env_variable("DB_HOST"),
            user=get_env_variable("DB_USER"),
            password=get_env_variable("DB_PASSWORD"),
            database=get_env_variable("DB_NAME")
        )
        db_manager.connect_database()
        insert_query = "INSERT INTO account (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        db_manager.execute_query("insert", insert_query, (first_name, last_name, email, password))  # Use plain password
        db_manager.close()
        print("Credentials inserted into the database")

def on_create_account_click():
    print("Create account button clicked!")

def on_connect_click():
    root.destroy()
    os.system("python Connect_interface.py")

# Adding UI elements to the frame

# Connect label
connect_label = ctk.CTkLabel(root, text="Register", font=("Arial", 16), bg_color="#4D4D4D")
connect_label.place(x=651, y=103)

def create_entry(placeholder_text, y_position):
    entry = ctk.CTkEntry(
        root,
        width=313.04,
        height=64,
        placeholder_text=placeholder_text,
        bg_color="#4D4D4D",
        fg_color="#2C2C2C",
        corner_radius=10,
        font=("Arial", 14)
    )
    entry.place(x=526, y=y_position)
    return entry

first_name_entry = create_entry("First Name", 148)
last_name_entry = create_entry("Last Name", 242)
email_entry = create_entry("Email", 336)

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
    show="*" 
)
password_entry.place(x=526, y=429)

# Error message label
error_label = ctk.CTkLabel(root, text="", font=("Arial", 12), bg_color="#4D4D4D", text_color="red")
error_label.place(x=526, y=500)

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
enter_button.place(x=740, y=591)

# Create account button
connect_button = ctk.CTkButton(
    root,
    width=98.66,
    height=64,
    text="Connect",
    corner_radius=10,
    bg_color="#4D4D4D",
    fg_color="#2C2C2C",
    command=on_connect_click  # Link function to button
)
connect_button.place(x=526, y=591)

root.mainloop()