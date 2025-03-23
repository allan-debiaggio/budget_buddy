import mysql.connector
from database_test import ManageDatabase

class Transaction(ManageDatabase):
    def __init__(self, database):
        self.database_name = database
        super().__init__(database)


    def return_transaction_informations(self, columns, conditions):
        """Return informations about a transaction based on columns and conditions
        columns = str and conditions = str"""        
        self.connect_database()
        query_type = "read"
        query = f"SELECT {columns} FROM transaction WHERE {conditions}"
        results = self.execute_query(query_type, query)
        self.close()

        columns = tuple(columns.split(", "))
        transaction = [dict(zip(columns, result)) for result in results]
        return transaction

    def execpt_column_history(self, transaction, column):
        """Return one type of information about the transaction to print the history in the graphic interface
        transaction = list that contains dict and column = str
        output = list"""
        history_column = [t[column] for t in transaction]
        return history_column


    def return_balance(self, id_user):
        """update the balance of user"""
        self.connect_database()
        query_type = "read"
        query = "SELECT SUM(amount) FROM transaction WHERE id_account = %s"
        value = (id_user, )
        balance = self.execute_query(query_type, query, value)
        self.close()
        return balance[0][0]


    def add_transaction(self, id_account, amount, date, type, category, reason):
        """Add a transaction in the table transaction"""
        self.connect_database()

        # recover the id of the category
        query_type = "read"
        query = f"SELECT id FROM category WHERE name = %s"
        value = (category, )
        result = self.execute_query(query_type, query, value)

        if not result:
            self.close()
            raise ValueError(f"The category '{category}' does not exist in the database.")
        
        id_category = result[0][0]

        # insert the transaction
        query_type = "insert"
        query = f"INSERT INTO transaction (id_account, amount, date, type, reason, id_category) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (id_account, amount, date, type, reason, id_category)
        self.execute_query(query_type, query, value)
        self.close()




