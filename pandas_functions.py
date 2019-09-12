import pandas as pd

def read_sql_query_to_dataframe(query, connection):
    df = pd.read_sql(query,con=connection)
    return df

def save_dataframe_to_excel(dataframe, excel_file_path, sheet_name):
    writer = pd.ExcelWriter(excel_file_path)
    dataframe.to_excel(writer,sheet_name)
    writer.save()

def read_excel_to_dataframe(excel_file_path, sheet_name):
    return pd.read_excel(excel_file_path, sheet_name = sheet_name)

def row_count_dataframe(dataframe):
    return dataframe.shape[0]

def column_count_dataframe(dataframe):
    return dataframe.shape[1]

def column_list_from_dataframe(dataframe):
    return list(dataframe)


