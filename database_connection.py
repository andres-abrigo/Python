import pymysql
import pandas as pd
import pandas_functions

user = 'username'
password = 'password'
port = port_number

IP = '127.0.0.1'
database_name = 'database_name'

with pymysql.connect(host= IP, port=port_number, user=user, passwd=password, db=database_name) as connection:
  query_table = """SELECT * FROM table"""
  dataframe_table = pandas_functions.dataframe_from_query(query, connection)
  print(dataframe_table.to_string())
  
                           
