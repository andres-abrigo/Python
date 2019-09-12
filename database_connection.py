import pymysql
import pandas as pd
import pandas_functions

user = 'username'
password = 'password'
port = port_number

IP = '127.0.0.1'
database_name = 'database_name'

connection = pymysql.connect(host= IP, port=port, user=user, passwd=password, db=database_name)

query_table = """SELECT * FROM ViewDebugInfo2"""

dataframe_table = pandas_functions.read_sql_query_to_dataframe(query_table, connection)

print(dataframe_table.to_string())

output_excel_path = 'result.xlsx'
sheet_name = 'sql_table'

pandas_functions.save_dataframe_to_excel(dataframe_table,output_excel_path, sheet_name)

connection.close()
