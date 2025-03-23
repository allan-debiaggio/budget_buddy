import secrets
import string
import bcrypt
import os
from dotenv import load_dotenv
from variable_test import get_env_variable

def generate_pepper(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    pepper = ''.join(secrets.choice(characters) for i in range(length))
    return pepper

# Generate a 16-character random pepper value
pepper_value = generate_pepper()
print(f"Generated PEPPER value: {pepper_value}")

class User:
    def __init__(self, first_name, last_name, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = self.hash_password(password)
        self.__id = None  # id of the user in the table user (utiliser la méthode read de la classe ManageDatabase pour le récupérer)

    # Getters
    @property
    def get_first_name(self):
        return self.__first_name

    @property
    def get_last_name(self):
        return self.__last_name

    @property
    def get_email(self):
        return self.__email

    @property
    def get_password(self):
        return self.__password

    @property
    def get_id(self):
        return self.__id

    # Setters
    @get_first_name.setter
    def set_first_name(self, first_name):
        self.__first_name = first_name
        # update the database?

    @get_last_name.setter
    def set_last_name(self, last_name):
        self.__last_name = last_name
        # update the database?

    @get_email.setter
    def set_email(self, email):
        self.__email = email
        # update the database?

    @get_password.setter
    def set_password(self, password):
        hash_password = self.hash_password(password)
        self.__password = hash_password
        # update the database?

    def insert_new_user(self):
        """add a new user in the table user, with password coded"""
        pass  # pour inserer dans la table user

    def hash_password(self, password):
        """hash the password of the user with bcrypt and a pepper"""
        # attention pour le hachage, il faut que password soit en string!!
        pepper = get_env_variable("PEPPER")
        peppered_password = password + pepper
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(peppered_password.encode(), salt)
        return hashed.decode()

    def check_password(self, input_password):
        """check if the password is correct"""
        pepper = get_env_variable("PEPPER")
        peppered_input_password = input_password + pepper
        check = bcrypt.checkpw(peppered_input_password.encode(), self.get_password.encode())
        return check

    def check_id(self, input_id):
        """check if the id of the user is correct"""
        # il faut pourvoir récupérer l'id de l'utilisateur dans la database
        # identifiant a plusieurs paramètres, genre input du last_name et de id, pour affiner la recherche
        return input_id == self.get_id()

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} {self.__email} {self.__password}"

# attention, il faut que je créer des methodes pour aller chercher les information dans la base de donnée
# pour les mettre dans les attributs de la classe User ?

def main():
    User1 = User("John", "Doe", "john.doe@gmail.com", "password")
    print(User1.check_password("pa"))
    print(User1.get_password)

if __name__ == "__main__":
    main()