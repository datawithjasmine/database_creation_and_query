import pandas as pd
import sqlite3


def table_query(database, query):
    conn = sqlite3.connect(database)
    dataframe = pd.read_sql_query(query, conn)
    conn.close()
    return dataframe


database_path = input("Enter the name of the database file (MUST INCLUDE '.db'): ")
query_data = input("Enter a query to see the results (USE TABLE NAME): ")

table = pd.DataFrame(table_query(database_path, query_data))

print(table.head(100).to_markdown(tablefmt="grid"))


