import customtkinter as ctk
from PIL import Image, ImageTk

# Configurer le thème
ctk.set_appearance_mode("dark")  # "dark", "light", or "system"
ctk.set_default_color_theme("blue")  # Thèmes disponibles : "blue", "green", "dark-blue"

# Créer la fenêtre principale
root = ctk.CTk()
root.title("Mon Interface CustomTkinter")
root.geometry("720x480")

# Charger l'image de fond
background_image = Image.open("screen_connect.png")  # Remplacez par le chemin de votre image
background_photo = ctk.CTkImage(light_image=background_image, dark_image=background_image, size=(800, 600))

# Créer un CTkLabel pour l'image de fond
background_label = ctk.CTkLabel(root, image=background_photo, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place l'image sur tout l'écran

# Ajouter un titre
title_label = ctk.CTkLabel(root, text="Bienvenue sur mon interface", font=("Arial", 24))
title_label.pack(pady=20)

# Ajouter un champ de texte
entry = ctk.CTkEntry(root, width=200, font=("Arial", 12))
entry.pack(pady=10)

# Ajouter un bouton
button = ctk.CTkButton(root, text="Cliquez-moi", corner_radius=10)
button.pack(pady=10)

# Lancer l'application
root.mainloop()
