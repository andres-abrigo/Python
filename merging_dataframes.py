import pandas as pd
import pandas_functions

excel_input_file_path = 'input.xlsx'
sheet_name_input_file = 'Sheet1'

dataframe_input = pandas_functions.read_excel_to_dataframe(excel_input_file_path,sheet_name_input_file)

excel_input_to_merge_path = 'input_to_merge.xlsx'
sheet_name_input_to_merge_file = 'Sheet1'

dataframe_input_to_merge = pandas_functions.read_excel_to_dataframe(excel_input_to_merge_path,sheet_name_input_to_merge_file)

merged_dataframe = pandas_functions.InnerJoin(dataframe_input, dataframe_input_to_merge,'Index','Index')

print('First dataframe: ')
print(dataframe_input.to_string())

print('Second dataframe: ')
print(dataframe_input_to_merge.to_string())
    
print('Merged dataframe: ')
print(merged_dataframe.to_string())


