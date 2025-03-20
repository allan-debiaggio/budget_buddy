import customtkinter as ctk
from PIL import Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Theme configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main window creation
root = ctk.CTk()
root.title("Budget Buddy")
root.geometry("1366x768")
root.resizable(False, False)  # Lock window resizing

# Loading background image
background_image = Image.open("asset/main_screen_backgraound.png")
background_photo = ctk.CTkImage(light_image=background_image, dark_image=background_image, size=(1366, 768))

# Creating label for background image
background_label = ctk.CTkLabel(root, image=background_photo, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Adding title on background image
title_label = ctk.CTkLabel(root, text="Hello {username}", font=("Arial", 26), bg_color="transparent")
title_label.place(x=27, y=34)

def on_filter_click():
    print("Filter button clicked!")
    # Add transaction filtering logic here

def on_transaction_click():
    print("Transaction button clicked!")
    # Add transaction display logic here

# Adding Balance frame
balance_frame = ctk.CTkFrame(
    root,
    width=380,
    height=218,
    fg_color="#4D4D4D",
    border_color="#000000", 
    border_width=2,  
)
balance_frame.place(x=162, y=88)

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

# Operations button
transaction_button = ctk.CTkButton(
    root,
    width=272,
    height=77,
    text="Operations",
    fg_color="#2C2C2C", 
    command=on_transaction_click,
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

root.mainloop()