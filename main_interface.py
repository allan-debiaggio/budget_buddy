import customtkinter as ctk
from PIL import Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database import ManageDatabase  # Import the ManageDatabase class
from variable_test import get_env_variable  # Import the get_env_variable function
import os
import subprocess

# Theme configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main window creation
root = ctk.CTk()
root.title("Budget Buddy")
root.geometry("1366x768")
root.resizable(False, False)  # Lock window resizing

# Loading background image
background_image = Image.open("asset/main_screen_background.png")
background_photo = ctk.CTkImage(light_image=background_image, dark_image=background_image, size=(1366, 768))

# Creating label for background image
background_label = ctk.CTkLabel(root, image=background_photo, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Retrieve user ID from environment variable
user_id = os.getenv("USER_ID")

# Retrieve user information from the database
db_manager = ManageDatabase(
    host=get_env_variable("DB_HOST"),
    user=get_env_variable("DB_USER"),
    password=get_env_variable("DB_PASSWORD"),
    database=get_env_variable("DB_NAME")
)
db_manager.connect_database()
query = "SELECT first_name, last_name FROM account WHERE id_account = %s"
result = db_manager.execute_query("read", query, (user_id,))
if result:
    first_name, last_name = result[0]
    username = f"{first_name} {last_name}"
else:
    username = "User"

def update_balance_and_history(order_by="date"):
    # Calculate current balance dynamically
    balance_query = """
        SELECT SUM(CASE WHEN type = 'Deposit' THEN amount ELSE -amount END) AS balance
        FROM transaction
        WHERE id_account = %s
    """
    balance_result = db_manager.execute_query("read", balance_query, (user_id,))
    if balance_result:
        current_balance = balance_result[0][0] if balance_result[0][0] is not None else 0.0
    else:
        current_balance = 0.0

    balance_label.configure(text=f"Current Balance: ${current_balance:.2f}")

    # Retrieve transaction history
    history_query = f"SELECT amount, date, reason, type FROM transaction WHERE id_account = %s ORDER BY {order_by}"
    history_result = db_manager.execute_query("read", history_query, (user_id,))

    history_text.delete("1.0", "end")
    for transaction in history_result:
        amount, date, reason, transaction_type = transaction
        history_text.insert("end", f"{date} - {transaction_type}: ${amount} - {reason}\n")

    # Update pie chart data based on the selected filter
    if order_by == "type":
        pie_query = """
            SELECT type, SUM(amount) as total
            FROM transaction
            WHERE id_account = %s
            GROUP BY type
        """
    elif order_by == "reason":
        pie_query = """
            SELECT reason, SUM(amount) as total
            FROM transaction
            WHERE id_account = %s
            GROUP BY reason
        """
    elif order_by == "amount":
        pie_query = """
            SELECT amount, COUNT(*) as total
            FROM transaction
            WHERE id_account = %s
            GROUP BY amount
        """
    else:  # Default to date
        pie_query = """
            SELECT date, SUM(amount) as total
            FROM transaction
            WHERE id_account = %s
            GROUP BY date
        """

    pie_result = db_manager.execute_query("read", pie_query, (user_id,))
    labels = [row[0] for row in pie_result]
    sizes = [row[1] for row in pie_result]

    # Update pie chart
    ax.clear()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%")
    canvas.draw()

# Adding title on background image
title_label = ctk.CTkLabel(root, text=f"Hello {username}", font=("Arial", 26), bg_color="transparent")
title_label.place(x=27, y=34)

# Adding Balance frame
balance_frame = ctk.CTkFrame(
    root,
    width=380,
    height=218,
    fg_color="#4D4D4D",
    border_color="#000000", 
    border_width=2,  
)
balance_frame.place(x=145, y=88)  # Adjusted x-coordinate to match pie_frame

balance_label = ctk.CTkLabel(balance_frame, text="Current Balance: $0.00", font=("Arial", 20))
balance_label.pack(pady=20)

# Adding History frame
history_frame = ctk.CTkFrame(
    root,
    width=508.11,
    height=690,
    fg_color="#4D4D4D",
    border_color="#000000", 
    border_width=2,  
)
history_frame.place(x=759, y=39)

history_label = ctk.CTkLabel(history_frame, text="Transaction History", font=("Arial", 20))
history_label.pack(pady=10)

history_text = ctk.CTkTextbox(history_frame, width=480, height=600)
history_text.pack(pady=10)

# Adding filter dropdown
filter_var = ctk.StringVar(value="date")
filter_dropdown = ctk.CTkComboBox(root, values=["date", "amount", "type", "reason"], variable=filter_var)
filter_dropdown.place(x=617, y=110)

def on_filter_click():
    print("Filter button clicked!")
    order_by = filter_var.get()
    update_balance_and_history(order_by)

def on_transaction_click(main_window):
    print("Transaction button clicked!")
    subprocess.Popen(["python", "transaction_interface.py"]).wait()
    main_window.destroy()
    subprocess.Popen(["python", "main_interface.py"])

def on_logout_click():
    print("Logout button clicked!")
    root.destroy()
    os.system("python Connect_interface.py")

# Operations button
transaction_button = ctk.CTkButton(
    root,
    width=272,
    height=77,
    text="Operations",
    fg_color="#2C2C2C", 
    command=lambda: on_transaction_click(root),
)
transaction_button.place(x=216, y=328)

# Filter button
filter_button = ctk.CTkButton(
    root,
    width=98.66,
    height=64,
    text="Filter",
    fg_color="#2C2C2C",
    command=on_filter_click, 
)
filter_button.place(x=617, y=37)

# Logout button
logout_button = ctk.CTkButton(
    root,
    width=150,
    height=50,
    text="Logout",
    fg_color="#2C2C2C",
    command=on_logout_click,
)
logout_button.place(x=1200, y=715)  # Adjusted y-coordinate to place the button lower

# Pie chart data
labels = ["Leisure & Entertainment", "Housing", "Energy", "Food", "Others"]
sizes = [15, 20, 35, 10, 20]

# Creating frame for pie chart
pie_frame = ctk.CTkFrame(
    root,
    width=380,
    height=218,
    fg_color="#4D4D4D",
    border_color="#000000", 
    border_width=2,
)
pie_frame.place(x=145, y=440)

# Creating pie chart
fig = Figure(figsize=(4, 2.5), dpi=100)
fig.patch.set_alpha(0.0)
ax = fig.add_subplot(111)
ax.set_facecolor('none')
ax.pie(sizes, labels=labels, autopct="%1.1f%%")

# Tkinter integration
canvas = FigureCanvasTkAgg(fig, master=pie_frame)
canvas.draw()
widget = canvas.get_tk_widget()
widget.configure(bg='#4D4D4D')
widget.pack(padx=10, pady=10)

def check_for_refresh():
    if os.path.exists("refresh.txt"):
        update_balance_and_history()
        os.remove("refresh.txt")
    root.after(1000, check_for_refresh)

update_balance_and_history()
check_for_refresh()

root.mainloop()