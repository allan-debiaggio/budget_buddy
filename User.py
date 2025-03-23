import bcrypt
import os
from dotenv import load_dotenv
from database_test import ManageDatabase

class User(ManageDatabase): 
    def __init__(self, first_name, last_name, email, password):
        super().__init__("bank")
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = self.hash_password(password)
        self.__id = self.get_user_id() 


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
        self.update_user_field("first_name", self.get_first_name)

    @get_last_name.setter 
    def set_last_name(self, last_name):
        self.__last_name = last_name
        self.update_user_field("last_name", self.get_last_name)

    @get_email.setter
    def set_email(self, email):
        self.__email = email
        self.update_user_field("email", self.get_email)

    @get_password.setter
    def set_password(self, password):
        hash_password = self.hash_password(password)
        self.__password = hash_password
        self.update_user_field("password", self.get_password)

    def update_user_field(self, field, value):
        """update a specific field in the table account"""
        self.connect_database()
        query_type = "alter"
        query = f"UPDATE account SET {field} = %s WHERE id_account = %s"
        values = (value, self.get_id())
        self.execute_query(query_type, query, values)
        self.close()

    def get_user_id(self):
        """return the id of the user based on the email"""
        self.connect_database()
        query_type = "read"
        query = "SELECT id_account FROM account WHERE email = %s"
        value = (self.get_email(),)
        result = self.execute_query(query_type, query, value)
        self.close()

        return result[0][0]

    def insert_new_user(self):
        """add a new user in the table user, with password coded"""
        self.connect_database()
        query_type = "insert"
        query = "INSERT INTO account(first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        values = (self.get_first_name(), self.get_last_name(), self.get_email(), self.get_password())
        self.execute_query(query_type, query, values)
        self.close()
        self.__id = self.get_user_id()

    def hash_password(self, password):
        """hash the password of the user with bcrypt and a pepper
        password = str"""
        pepper = self.get_env_variable("PEPPER")
        peppered_password = password + pepper
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(peppered_password.encode(), salt)
        return hashed.decode()

    def check_password(self, input_password, input_id):
        """check if the password is correct"""
        self.connect_database()

        query_type = "read"
        query = "SELECT password FROM account WHERE id_account = %s"
        value = (input_id, )
        result = self.execute_query(query_type, query, value)
        self.close()

        if not result:
            return False
        
        storred_password = result[0][0]
        pepper = self.get_env_variable("PEPPER")
        peppered_input_password = input_password + pepper

        check = bcrypt.checkpw(peppered_input_password.encode(), storred_password.encode())
        return check

    def return_client_information(self, id_user):
        """Return the first name and last name of a user based on the id"""
        self.connect_database()
        query_type = "read"
        query = f"SELECT first_name, last_name FROM account WHERE id_account = %s"
        value = (id_user, )
        result = self.execute_query(query_type, query, value)

        if not result:
            self.close()
            raise ValueError(f"The user with id '{id_user}' does not exist in the database")
        
        client = {
            "id": id_user,
            "first_name": result[0][0],
            "last_name": result[0][1]
        }
        self.close()
        return client


    def __str__(self):
        return f"{self.__first_name} {self.__last_name} {self.__email} {self.__password}"
    


def main():
    User1 = User("John", "Doe", "john.doe@gmail.com", "password")
    print(User1.check_password("pa"))
    print(User1.get_password)


if __name__ == "__main__":
    main()