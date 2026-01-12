import MySQLdb

try:
    db = MySQLdb.connect("localhost", "root", "")
    cursor = db.cursor()
    cursor.execute("DROP DATABASE IF EXISTS airline_system")
    cursor.execute("CREATE DATABASE airline_system")
    print("Database 'airline_system' reset successfully.")
    db.close()
except Exception as e:
    print(f"Error resetting database: {e}")
