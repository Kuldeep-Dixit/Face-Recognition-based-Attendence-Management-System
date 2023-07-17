# import pyodbc
# import pandas as pd
# import os
# from datetime import datetime

# # create sql connection
# connection = pyodbc.connect(driver = '{MySQL ODBC 8.0 ANSI Driver}', host ='localhost',
#                             database="face_recognizer",trusted_connection="yes")

# #  sql command to read query 
# sqlQuery = "SELECT * FROM student"

# # getting the data from sql into pandas dataframe
# df = pd.read_sql(sql = sqlQuery, con = connection)

# # Export data on the desktop
# df.to_csv(os.environ["userprofile"]+"\\Desktop\\xyz\\"+"Student data"+
#           datetime.now().strftime("%d-%b-%Y %H%M%S")+".csv",index=False)



# # print(pyodbc.drivers())


import pandas as pd
import sqlite3
import mysql.connector
from xlsxwriter import Workbook
from datetime import datetime
from time import strftime


sql = "SELECT * FROM face_recognizer.student;"
db = mysql.connector.connect(host="localhost", database="face_recognizer", user="root", passwd="Kuldeep@16", use_pure=True)
df = pd.read_sql(sql, db)
df.head()
df.to_excel(datetime.now().strftime("%b%d%Y_%H%M.xlsx"), index=False)
db.close()



