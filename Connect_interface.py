import customtkinter as ctk
from PIL import Image

# Configuration du thème
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

# Création de la fenêtre principale
root = ctk.CTk()
root.title("Interface with Background Image")
root.geometry("1366x768")
root.resizable(False, False)

# Chargement de l'image de fond
background_image = Image.open("asset/screen_connect.png")
background_photo = ctk.CTkImage(light_image=background_image, dark_image=background_image, size=(1366, 768))

# Création d'un label pour l'image de fond
background_label = ctk.CTkLabel(root, image=background_photo, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Ajout d'un titre sur l'image de fond
title_label = ctk.CTkLabel(root, text="Budget Buddy", font=("Arial", 42), bg_color="transparent")
title_label.place(relx=0.5, rely=0.1, anchor="center")

# Création d'un cadre (frame) pour regrouper les éléments
frame = ctk.CTkFrame(root, width=360, height=414, fg_color="#4D4D4D", corner_radius=0)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Définition des fonctions pour les boutons
def on_identifier_click():
    print("Bouton Identifier cliqué !")

def on_password_click():
    print("Bouton Password cliqué !")

def on_enter_click():
    print("Bouton Enter cliqué !")

def on_create_account_click():
    print("Bouton Create an account cliqué !")

# Ajout des éléments d'interface utilisateur dans le cadre

# Label "Connect"
connect_label = ctk.CTkLabel(root, text="Connect", font=("Arial", 10), bg_color="#4D4D4D")
connect_label.place(x=665, y=203)

# Bouton "Identifier"
identifier_button = ctk.CTkButton(
    root,
    width=313.04,
    height=64,
    text="Identifier",
    corner_radius=10,
    bg_color="#4D4D4D",
    fg_color="#2C2C2C",
    command=on_identifier_click  
)
identifier_button.place(x=527.43, y=238.4)

# Bouton "Password"
password_button = ctk.CTkButton(
    root,
    width=313.04,
    height=64,
    text="Password",
    corner_radius=10,
    bg_color="#4D4D4D",
    fg_color="#2C2C2C",
    command=on_password_click 
)
password_button.place(x=527.43, y=320)

# Bouton "Enter"
enter_button = ctk.CTkButton(
    root,
    width=98.66,
    height=64,
    text="Enter",
    corner_radius=10,
    bg_color="#4D4D4D",
    fg_color="#2C2C2C",
    command=on_enter_click 
)
enter_button.place(x=741.81, y=473.6)

# Bouton "Create an account"
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

# Lancement de la boucle principale de l'interface
root.mainloop()