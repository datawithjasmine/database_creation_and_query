# TABLE-QUERY PROGRAM by JASMINE MITCHELL

#              --- COMMENTS ---

# 1. I IMPORTED THE FOLLOWING LIBRARIES
#    - Pandas: to turn the queries into a DataFrame.
#    - SQLite3: to perform SQL queries and connect to the database file.

import sqlite3
import pandas as pd

# 2. The TABLE_QUERY function is to create a table from the database
#           file given so that the user can perform SQL queries


def table_query(database, query):
    conn = sqlite3.connect(database)
    dataframe = pd.read_sql_query(query, conn)
    conn.close()
    return dataframe

# 3. The EXPORT_EXCEL function allow users to export their queried data
#     into an Excel file format so that they can perform data analysis


def export_excel(queried_data, filename):
    # queried_data = pd.DataFrame(queried_data)
    queried_data.to_excel(filename, sheet_name="Sheet_1")
    print("Your query has been successfully exported as an Excel file.")

# 4. The user will be prompted for the name of the database file and to create
#       a SQL query. The result will be a DataFrame table that will only
#       show the first 100 rows of the table. I did this due to many csv
#                     files containing thousands of rows.
#      The user can decide if they want to convert the query data into an
#                   Excel file or create another query.
#         The program ends when the user enter the exit commands.


database_path = input("Enter the name of the database file (MUST INCLUDE '.db'): ")

query_data = input("Enter a query to see the first 100 results (USE TABLE NAME): ")

table = pd.DataFrame(table_query(database_path, query_data))

print(table.head(100).to_markdown(tablefmt="grid"))

excel_convert = input("Would you like to export this table as an Excel file? (yes/no): ").lower()

while True:
    if excel_convert == 'yes':
        name = input("What would you like to name this file? (MUST INCLUDE '.xlsx'): ")
        export_excel(table, name)
        break
    elif excel_convert == "no":
        break
    else:
        raise ValueError("Invalid response. Please enter a yes or no.")


ans = input("Would you like to make a new query or quit the program? Press Q for quit. ").lower()

while True:
    if ans == "q":
        break
    elif ans == "yes":
        query_data = input("Enter a query to see the first 100 results (USE TABLE NAME). Press 0 to end querying: ")
        if query_data == "0":
            break
        else:
            table = pd.DataFrame(table_query(database_path, query_data))
            print(table.head(100).to_markdown(tablefmt="grid"))
            excel_convert = input("Would you like to export this table as an Excel file? (yes/no): ").lower()

            while True:
                if excel_convert == 'yes':
                    name = input("What would you like to name this file? (MUST INCLUDE '.xlsx'): ")
                    export_excel(table, name)
                    break
                elif excel_convert == "no":
                    break
                else:
                    raise ValueError("Invalid response. Please enter a yes or no.")

    else:
        raise ValueError("Invalid response. Enter yes to continue or Q to quit!")

print("-- END OF PROGRAM --")