import pymysql
import pandas as pd
import pandas_functions

user = 'username'
password = 'password'
port = 3303

IP = '127.0.0.1'
database_name = 'database_name'

with pymysql.connect(host= IP, port=port, user=user, passwd=password, db=database_name) as connection:
  query_table = """SELECT * FROM table"""
  dataframe_table = pandas_functions.dataframe_from_query(query, connection)
  print(dataframe_table.to_string())
  
                           
