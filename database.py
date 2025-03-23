# import customtkinter as ctk
# from PIL import Image
# import os
# import re  # Add this import for regular expressions
# import mysql.connector
# from dotenv import load_dotenv

# # Theme configuration
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# # Main window creation
# root = ctk.CTk()
# root.title("Budget Buddy")
# root.geometry("1366x768")
# root.resizable(False, False) 

# # Loading background image
# background_image = Image.open("asset/register_background.png")
# background_photo = ctk.CTkImage(light_image=background_image, dark_image=background_image, size=(1366, 768))

# # Creating label for background image
# background_label = ctk.CTkLabel(root, image=background_photo, text="")
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

# # Creating frame to group elements
# frame = ctk.CTkFrame(root, width=360, height=604, fg_color="#4D4D4D", corner_radius=0)
# frame.place(relx=0.5, rely=0.5, anchor="center")

# # Button functions definition
# def validate_email(email):
#     return "@" in email and "." in email

# def validate_password(password):
#     if len(password) < 10:
#         return False
#     if not re.search(r"[A-Z]", password):
#         return False
#     if not re.search(r"[a-z]", password):
#         return False
#     if not re.search(r"[0-9]", password):
#         return False
#     if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#         return False
#     return True

# def on_enter_click():
#     first_name = first_name_entry.get() 
#     last_name = last_name_entry.get()
#     email = email_entry.get() 
#     password = password_entry.get() 

#     if not validate_email(email) or not validate_password(password):
#         error_label.configure(text="Invalid information")
#     else:
#         error_label.configure(text="")
#         print(f"First name: {first_name}, Last name: {last_name}, Email: {email}, Password: {password}")
        
#         # Insert credentials into the database
#         db_manager = ManageDatabase(host="localhost", user="your_username", password="your_password", database="bank")
#         db_manager.connect_database()
#         insert_query = "INSERT INTO account (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
#         db_manager.execute_query("insert", insert_query, (first_name, last_name, email, password))
#         db_manager.close()
#         print("Credentials inserted into the database")

# def on_create_account_click():
#     print("Create account button clicked!")

# def on_connect_click():
#     root.destroy()
#     os.system("python Connect_interface.py")

# # Adding UI elements to the frame

# # Connect label
# connect_label = ctk.CTkLabel(root, text="Register", font=("Arial", 16), bg_color="#4D4D4D")
# connect_label.place(x=651, y=103)

# def create_entry(placeholder_text, y_position):
#     entry = ctk.CTkEntry(
#         root,
#         width=313.04,
#         height=64,
#         placeholder_text=placeholder_text,
#         bg_color="#4D4D4D",
#         fg_color="#2C2C2C",
#         corner_radius=10,
#         font=("Arial", 14)
#     )
#     entry.place(x=526, y=y_position)
#     return entry

# first_name_entry = create_entry("First Name", 148)
# last_name_entry = create_entry("Last Name", 242)
# email_entry = create_entry("Email", 336)

# # Password entry field
# password_entry = ctk.CTkEntry(
#     root,
#     width=313.04,
#     height=64,
#     placeholder_text="Password",
#     bg_color="#4D4D4D",
#     fg_color="#2C2C2C",
#     corner_radius=10,
#     font=("Arial", 14),
#     show="*" 
# )
# password_entry.place(x=526, y=429)

# # Error message label
# error_label = ctk.CTkLabel(root, text="", font=("Arial", 12), bg_color="#4D4D4D", text_color="red")
# error_label.place(x=526, y=500)

# # Enter button
# enter_button = ctk.CTkButton(
#     root,
#     width=98.66,
#     height=64,
#     text="Enter",
#     corner_radius=10,
#     bg_color="#4D4D4D",
#     fg_color="#2C2C2C",
#     command=on_enter_click  # Link function to button
# )
# enter_button.place(x=740, y=591)

# # Create account button
# connect_button = ctk.CTkButton(
#     root,
#     width=98.66,
#     height=64,
#     text="Connect",
#     corner_radius=10,
#     bg_color="#4D4D4D",
#     fg_color="#2C2C2C",
#     command=on_connect_click  # Link function to button
# )
# connect_button.place(x=526, y=591)

# root.mainloop()

import mysql.connector
from dotenv import load_dotenv
import os

class ManageDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect_database(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        print("Database connected")

    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database connection closed")

    def insert(self, query, values):
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Record inserted")

    def read(self, query, values=None):
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    def delete(self, query, values):
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Record deleted")

    def alter(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        print("Table altered")

    def execute_query(self, query_type, query, values=None):
        """Execute a query based on the query type"""
        if query_type == "insert":
            self.insert(query, values)
        elif query_type == "read":
            return self.read(query, values)
        elif query_type == "delete":
            self.delete(query, values)
        elif query_type == "alter":
            self.alter(query)
        else:
            raise ValueError(f"Unknown query type: {query_type}")

# Example usage
if __name__ == "__main__":
    db_manager = ManageDatabase(host="localhost", user="your_username", password="your_password", database="bank")
    db_manager.connect_database()

    # Example dynamic queries
    # db_manager.execute_query("insert", "INSERT INTO table_name (column1, column2) VALUES (%s, %s)", (value1, value2))
    # results = db_manager.execute_query("read", "SELECT * FROM table_name")
    # db_manager.execute_query("delete", "DELETE FROM table_name WHERE condition", (value,))
    # db_manager.execute_query("alter", "ALTER TABLE table_name ADD column_name datatype")

    db_manager.close()