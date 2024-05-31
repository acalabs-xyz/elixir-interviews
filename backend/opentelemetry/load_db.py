import sqlite3
import pandas as pd

table_name = "traces"


def load_db():
    # Establish a connection to an in-memory SQLite database
    conn = sqlite3.connect(":memory:")

    # Read the CSV file into a pandas DataFrame
    csv_file_path = "traces.csv"
    df = pd.read_csv(csv_file_path)

    # Insert the DataFrame data into a new SQLite table
    df.to_sql(table_name, conn, index=False, if_exists="replace")

    # Remember to close the connection when done
    return conn
