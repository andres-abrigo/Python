import pandas as pd

def read_sql_query_to_dataframe(query, connection):
    df = pd.read_sql(query,con=connection)
    return df
