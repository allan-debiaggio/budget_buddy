import mysql.connector
from dotenv import load_dotenv
import os

class ManageDatabase:
    def __init__(self, bank):
        self.connection = None
        self.cursor = None
        self.bank = bank

    def connect_database(self):
        self.connection = mysql.connector.connect(
            user="root",
            password=self.get_env_variable("PASSWORD"),
            host="127.0.0.1",
            database=self.bank
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

    def read(self, query):
        self.cursor.execute(query)
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

    def get_env_variable(self, var_name):
        """Get a variable from the .env file"""
        load_dotenv()
        var = os.getenv(var_name)
        if not var:
            raise ValueError(f"{var_name} is not set in the .env file")
        return var

    def execute_query(self, query_type, query, values=None):
        """Execute a query based on the query type"""
        if query_type == "insert":
            self.insert(query, values)
        elif query_type == "read":
            return self.read(query)
        elif query_type == "delete":
            self.delete(query, values)
        elif query_type == "alter":
            self.alter(query)
        else:
            raise ValueError(f"Unknown query type: {query_type}")

# Example usage
db_manager = ManageDatabase("bank")
db_manager.connect_database()

# Example dynamic queries
# db_manager.execute_query("insert", "INSERT INTO table_name (column1, column2) VALUES (%s, %s)", (value1, value2))
# results = db_manager.execute_query("read", "SELECT * FROM table_name")
# db_manager.execute_query("delete", "DELETE FROM table_name WHERE condition", (value,))
# db_manager.execute_query("alter", "ALTER TABLE table_name ADD column_name datatype")

db_manager.close()