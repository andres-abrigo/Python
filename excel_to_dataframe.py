import pandas as pd
import pandas_functions

excel_path = 'input.xlsx'
sheet_name = 'Sheet1'
dataframe = pandas_functions.read_excel_to_dataframe(excel_path,sheet_name)

print(dataframe.to_string())

print('Column list: ')
column_list = pandas_functions.column_list_from_dataframe(dataframe)
print(column_list)

print('Row count: ')
row_count = pandas_functions.row_count_dataframe(dataframe)
print(row_count)

print('Column count: ')
column_count = pandas_functions.column_count_dataframe(dataframe)
print(column_count)
