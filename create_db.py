import MySQLdb

try:
    db = MySQLdb.connect("localhost", "root", "")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS airline_system")
    print("Database 'airline_system' created successfully.")
    db.close()
except Exception as e:
    print(f"Error creating database: {e}")
