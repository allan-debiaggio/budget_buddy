from Connect_interface import root, on_enter_click, on_create_account_click
from database import ManageDatabase
from User import User

def main():
    # Initialize the database manager
    db_manager = ManageDatabase("users.db")
    db_manager.connect_database()

    # Example usage of User class
    user = User("John", "Doe", "john.doe@gmail.com", "Password123!")
    print(user)

    # Example dynamic queries
    # Insert a new user into the database
    insert_query = "INSERT INTO account (first_name, last_name, email, password) VALUES (?, ?, ?, ?)"
    db_manager.execute_query("insert", insert_query, (user.get_first_name(), user.get_last_name(), user.get_email(), user.get_password()))

    # Read users from the database
    read_query = "SELECT * FROM account"
    users = db_manager.execute_query("read", read_query)
    print(users)

    # Close the database connection
    db_manager.close()

    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    main()