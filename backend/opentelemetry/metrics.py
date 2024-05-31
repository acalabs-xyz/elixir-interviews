from load_db import load_db, table_name

if __name__ == "__main__":
    conn = load_db()

    cursor = conn.cursor()

    # Get the schema of the table
    cursor.execute(f"PRAGMA table_info({table_name})")
    schema_info = cursor.fetchall()
    for column in schema_info:
        print(column)

    # Execute a query
    query = f"""
    SELECT * FROM {table_name}
    LIMIT 1
    """
    result = cursor.execute(query)
    print(cursor.fetchone())

    conn.close()
