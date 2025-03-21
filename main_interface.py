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
    selected_filter = filter_combobox.get()
    if selected_filter == "Category":
        category_window = ctk.CTkToplevel(root)
        category_window.title("Select Category")
        category_window.geometry("300x400")
        
        category_combobox = ctk.CTkComboBox(
            category_window,
            width=200,
            height=64,
            values=category_values,
            bg_color="transparent",
            fg_color="#2C2C2C",
            button_color="#2C2C2C",
            button_hover_color="#1C1C1C",
            border_color="#2C2C2C",
            corner_radius=10,
            font=("Arial", 14),
            dropdown_font=("Arial", 14),
            state="readonly"
        )
        category_combobox.pack(pady=20)
        category_combobox.set("Select Category")
        
        def apply_category():
            selected_category = category_combobox.get()
            print(f"Filtering by Category: {selected_category}")
            category_window.destroy()
            
        apply_button = ctk.CTkButton(
            category_window,
            text="Apply",
            command=apply_category,
            width=100,
            height=32,
            fg_color="#2C2C2C"
        )
        apply_button.pack(pady=10)
    
    elif selected_filter == "Date Range":
        print("Opening date range picker...")
    else:
        print(f"Filtering by: {selected_filter}")

def on_transaction_click():
    selected_operation = operation_combobox.get()
    print(f"Selected operation: {selected_operation}")

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

# Remplacer le bouton Operations par un ComboBox
operation_values = ["Deposit", "Withdrawal", "Transaction"]
operation_combobox = ctk.CTkComboBox(
    root,
    width=272,
    height=77,
    values=operation_values,
    bg_color="transparent",
    fg_color="#2C2C2C",
    button_color="#2C2C2C",
    button_hover_color="#1C1C1C",
    border_color="#2C2C2C",
    corner_radius=10,
    font=("Arial", 14),
    dropdown_font=("Arial", 14),
    state="readonly"
)
operation_combobox.place(x=216, y=328)
operation_combobox.set("Select Operation")

# Define filter options
filter_values = [
    "Date",
    "Category",  # This will have sub-options
    "Type",
    "Ascending",
    "Descending",
    "Date Range"
]

# Category sub-options remain the same
category_values = [
    "Housing",
    "Leisure & Entertainment",
    "Other",
    "Food",
    "Energy"
]

def on_filter_select(choice):
    if choice == "Category":
        category_window = ctk.CTkToplevel(root)
        category_window.title("Select Category")
        category_window.geometry("300x400")
        
        category_combobox = ctk.CTkComboBox(
            category_window,
            width=200,
            height=64,
            values=category_values,
            bg_color="transparent",
            fg_color="#2C2C2C",
            button_color="#2C2C2C",
            button_hover_color="#1C1C1C",
            border_color="#2C2C2C",
            corner_radius=10,
            font=("Arial", 14),
            dropdown_font=("Arial", 14),
            state="readonly"
        )
        category_combobox.pack(pady=20)
        category_combobox.set("Select Category")
        
        def apply_filter():
            selected_category = category_combobox.get()
            if selected_category != "Select Category":
                print(f"Filtering by category: {selected_category}")
            category_window.destroy()
        
        apply_button = ctk.CTkButton(
            category_window,
            text="Apply",
            command=apply_filter,
            width=100,
            height=32,
            fg_color="#2C2C2C"
        )
        apply_button.pack(pady=10)
    else:
        print(f"Selected filter: {choice}")

# Create filter combobox
filter_combobox = ctk.CTkComboBox(
    root,
    width=200,
    height=64,
    values=filter_values,
    bg_color="transparent",
    fg_color="#2C2C2C",
    button_color="#2C2C2C",
    button_hover_color="#1C1C1C",
    border_color="#2C2C2C",
    corner_radius=10,
    font=("Arial", 14),
    dropdown_font=("Arial", 14),
    state="readonly",
    command=on_filter_select
)
filter_combobox.place(x=550, y=37)
filter_combobox.set("Select Filter")

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
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct="%1.1f%%",
                                 wedgeprops={'edgecolor': 'black',
                                           'linewidth': 1.5})         

# Tkinter integration
canvas = FigureCanvasTkAgg(fig, master=pie_frame)
canvas.draw()
widget = canvas.get_tk_widget()
widget.configure(bg='#4D4D4D')
widget.pack(padx=10, pady=10)

root.mainloop()