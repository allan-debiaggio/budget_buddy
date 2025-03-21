import customtkinter as ctk
from PIL import Image
import re

def validate_amount(P):
    # Allow empty field
    if P == "":
        return True
        
    # Check if input matches the pattern: digits + optional decimal point + exactly 2 digits
    try:
        # If there's a decimal point
        if '.' in P:
            whole, decimal = P.split('.')
            # Ensure there are exactly 2 digits after decimal
            if len(decimal) > 2:
                return False
            # Ensure it's a valid positive number
            if float(P) >= 0:
                return True
        # If no decimal point, allow only digits
        else:
            return P.isdigit()
    except ValueError:
        return False
    return False

# Add date validation function
def validate_date(P):
    # Allow empty field
    if P == "":
        return True
    
    # Check if input matches DD/MM/YY pattern allowing incomplete input
    if len(P) > 8:  # Max length for DD/MM/YY format
        return False
        
    parts = P.split('/')
    
    if len(parts) > 3:  # Max 3 parts (DD/MM/YY)
        return False
        
    for part in parts:
        if not (part.isdigit() or part == ''):
            return False
            
        if len(part) > 2:  # Each part should be max 2 digits
            return False
    
    # If we have a complete date, validate the values
    if len(parts) == 3 and all(parts):
        try:
            day, month, year = map(int, parts)
            # Validate day
            if not (1 <= day <= 31):
                return False
            # Validate month
            if not (1 <= month <= 12):
                return False
            # Validate year
            if not (0 <= year <= 99):
                return False
            return True
        except ValueError:
            return False
            
    return True

# Theme configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main window creation
root = ctk.CTk()
root.title("Budget Buddy")
root.geometry("1366x768")
root.resizable(False, False) 

# Loading background image
background_image = Image.open("asset/transaction_background.png")
background_photo = ctk.CTkImage(light_image=background_image, dark_image=background_image, size=(1366, 768))

# Creating label for background image
background_label = ctk.CTkLabel(root, image=background_photo, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Creating frame to group elements
frame = ctk.CTkFrame(root, width=360, height=604, fg_color="#4D4D4D", corner_radius=0)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Button functions definition
def on_enter_click():
    amount = amount_entry.get() 
    date = date_entry.get()
    transaction_type = type_combobox.get()  # Changed from type_entry to type_combobox
    reason = reason_entry.get() 

    print(f"Amount: {amount}, Date: {date}, Type: {transaction_type}, Reason: {reason}")
    # Add login validation logic here

def on_create_account_click():
    print("Create account button clicked!")


def on_connect_click():
    print("Connect button clicked!")


# Adding UI elements to the frame

# Connect label
connect_label = ctk.CTkLabel(root, text="Transaction", font=("Arial", 16), bg_color="#4D4D4D")
connect_label.place(x=651, y=103)

# Modifiez la fonction create_entry pour ajouter la validation
def create_entry(placeholder_text, y_position, validate_cmd=None):
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
    
    if validate_cmd:
        # Register validation command
        vcmd = (root.register(validate_cmd), '%P')
        entry.configure(validate='key', validatecommand=vcmd)
    
    entry.place(x=526, y=y_position)
    return entry

# Modifiez la création de amount_entry
amount_entry = create_entry("Amount", 148, validate_amount)
date_entry = create_entry("Date (DD/MM/YY)", 242, validate_date)

# Replace type_entry creation with a ComboBox
type_values = ["Deposit", "Withdrawal", "Transaction"]
type_combobox = ctk.CTkComboBox(
    root,
    width=313.04,
    height=64,
    values=type_values,
    bg_color="#4D4D4D",
    fg_color="#2C2C2C",
    button_color="#2C2C2C",
    button_hover_color="#1C1C1C",
    border_color="#2C2C2C",
    corner_radius=10,
    font=("Arial", 14),
    dropdown_font=("Arial", 14),
    state="readonly"  # Prevents manual entry
)
type_combobox.place(x=526, y=336)
type_combobox.set("Select type")  # Default text

# reason entry field
reason_entry = ctk.CTkEntry(
    root,
    width=313.04,
    height=64,
    placeholder_text="Reason",
    bg_color="#4D4D4D",
    fg_color="#2C2C2C",
    corner_radius=10,
    font=("Arial", 14),
    show="*" 
)
reason_entry.place(x=526, y=429)

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

# Back button
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