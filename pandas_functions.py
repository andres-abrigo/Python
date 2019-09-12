import pandas as pd

def read_sql_query_to_dataframe(query, connection):
    df = pd.read_sql(query,con=connection)
    return df

def save_dataframe_to_excel(dataframe, excel_file_path, sheet_name):
    writer = pd.ExcelWriter(excel_file_path)
    dataframe.to_excel(writer,sheet_name)
    writer.save()
    
