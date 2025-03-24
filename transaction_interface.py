import customtkinter as ctk
from PIL import Image
from database import ManageDatabase  # Import the ManageDatabase class
from variable_test import get_env_variable  # Import the get_env_variable function
import os
import subprocess

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
root.title("Add Transaction")
root.geometry("600x400")
root.resizable(False, False)  # Lock window resizing

# Loading background image
background_image = Image.open("asset/transaction_background.png")
background_photo = ctk.CTkImage(light_image=background_image, dark_image=background_image, size=(600, 400))

# Creating label for background image
background_label = ctk.CTkLabel(root, image=background_photo, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Adding title
title_label = ctk.CTkLabel(root, text="Add Transaction", font=("Arial", 24), bg_color="transparent")
title_label.place(x=200, y=20)

# Adding input fields
amount_label = ctk.CTkLabel(root, text="Amount", font=("Arial", 14), bg_color="transparent")
amount_label.place(x=200, y=70)
amount_entry = ctk.CTkEntry(root, width=200)
amount_entry.place(x=200, y=100)

date_label = ctk.CTkLabel(root, text="Date (YYYY-MM-DD)", font=("Arial", 14), bg_color="transparent")
date_label.place(x=200, y=130)
date_entry = ctk.CTkEntry(root, width=200)
date_entry.place(x=200, y=160)

type_label = ctk.CTkLabel(root, text="Type", font=("Arial", 14), bg_color="transparent")
type_label.place(x=200, y=190)
type_combobox = ctk.CTkComboBox(root, values=["Deposit", "Withdrawal", "Transfer"], width=200)
type_combobox.place(x=200, y=220)

reason_label = ctk.CTkLabel(root, text="Reason", font=("Arial", 14), bg_color="transparent")
reason_label.place(x=200, y=250)
reason_entry = ctk.CTkEntry(root, width=200)
reason_entry.place(x=200, y=280)

def on_enter_click(main_window):
    amount = amount_entry.get()
    date = date_entry.get()
    transaction_type = type_combobox.get()
    reason = reason_entry.get()
    user_id = os.getenv("USER_ID")

    db_manager = ManageDatabase(
        host=get_env_variable("DB_HOST"),
        user=get_env_variable("DB_USER"),
        password=get_env_variable("DB_PASSWORD"),
        database=get_env_variable("DB_NAME")
    )
    db_manager.connect_database()
    insert_query = "INSERT INTO transaction (amount, date, reason, type, id_account) VALUES (%(amount)s, %(date)s, %(reason)s, %(type)s, %(user_id)s)"
    db_manager.execute_query("insert", insert_query, {'amount': amount, 'date': date, 'reason': reason, 'type': transaction_type, 'user_id': user_id})
    db_manager.update_balance(user_id)  # Update the balance
    db_manager.close()
    print("Transaction added")
    root.destroy()
    main_window.destroy()
    # Reopen the main interface
    subprocess.Popen(["python", "main_interface.py"])

enter_button = ctk.CTkButton(root, text="Enter", command=lambda: on_enter_click(root))
enter_button.place(x=250, y=320)

root.mainloop()