import customtkinter as ctk
from PIL import Image

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
def on_enter_click():
    first_name = first_name_entry.get() 
    last_name = last_name_entry.get()
    email = email_entry.get() 
    password = password_entry.get() 

    print(f"First name : {first_name}, Last name :{last_name},Email :{email}, Password: {password}")
    # Add login validation logic here

def on_create_account_click():
    print("Create account button clicked!")


def on_connect_click():
    print("Connect button clicked!")


# Adding UI elements to the frame

# Connect label
connect_label = ctk.CTkLabel(root, text="Register", font=("Arial", 16), bg_color="#4D4D4D")
connect_label.place(x=651, y=103)

def create_entry(placeholder_text, y_position):
    return ctk.CTkEntry(
        root,
        width=313.04,
        height=64,
        placeholder_text=placeholder_text,
        bg_color="#4D4D4D",
        fg_color="#2C2C2C",
        corner_radius=10,
        font=("Arial", 14)
    ).place(x=526, y=y_position)

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