import sqlite3
import csv


def sqlite_table_to_csv(db_path, table_name, csv_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute the query to fetch all data from the table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Get the column names
    columns = [description[0] for description in cursor.description]

    # Write the rows to the CSV file
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(columns)  # Write the column headers
        csv_writer.writerows(rows)  # Write the table rows

    # Close the connection
    conn.close()
    print(f"Table '{table_name}' exported to '{csv_path}' successfully.")


# Example usage
sqlite_table_to_csv("../leonardo/prompts.db", "prompts", "prompts.csv")
