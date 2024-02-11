# %%
import pandas as pd 
addresses = pd.read_csv('/Users/username/Downloads/file_name/name.csv', index_col=False, delimiter = ',', dtype={2 : "string", 7 : "string"}) 
print(addresses.head())
# %%
import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='here_is_your_user',  
                        password='here_is_your_password')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE Luminor")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)
print(conn.close())
if not conn.is_connected():
    print("Connection closed")
# %%
