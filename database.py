import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv("PASSWORD")

mydb = mysql.connector.connect(
    user = "root",
    password = PASSWORD,
    host = "127.0.0.1",
    database = "bank"
)

if mydb != None :
    print("Connection... ESTABLISHED ! WOUUUUSHHHHHHH")