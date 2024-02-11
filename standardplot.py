# %%
import pandas as pd
empdata = pd.read_csv('/Users/user/Downloads/sending.csv', index_col=False, delimiter = ',')
empdata.head()
# %%
import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='user',  
                        password='password')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE Phish")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)
conn.close()
if not conn.is_connected():
    print("Connection closed")
# %%
import mysql.connector
from mysql.connector import Error
import mysql
try:
    conn = mysql.connector.connect(host='localhost', database='database', user='user', password='password')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS sending;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE sending(from_address varchar(255),subject varchar(255),originating_ip varchar(255),date varchar(255),email_recipient varchar(255),count varchar(255))")
        print("Table is created....")
        #loop through the data frame
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO Phish.sending VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
                        # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
            print("Record inserted")
    sql = "SELECT * FROM Phish.sending"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
            print(i)
except Error as e:
            print("Error while connecting to MySQL", e)
conn.close()
if not conn.is_connected():
    print("Connection closed")
# %%
