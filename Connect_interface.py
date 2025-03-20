import customtkinter as ctk
from PIL import Image

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
def on_enter_click():
    username = username_entry.get()  # Get text from username field
    password = password_entry.get()  # Get text from password field
    print(f"Username: {username}, Password: {password}")
    # Add login validation logic here

def on_create_account_click():
    print("Create account button clicked!")
    # Add account creation logic here

# Adding UI elements to the frame

# Connect label
connect_label = ctk.CTkLabel(root, text="Connect", font=("Arial", 10), bg_color="#4D4D4D")
connect_label.place(x=665, y=203)

# Username entry field
username_entry = ctk.CTkEntry(
    root,
    width=313.04,
    height=64,
    placeholder_text="Username",
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