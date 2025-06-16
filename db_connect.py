import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',         # or your database host/IP
            user='your_username',     # e.g., 'root'
            password='your_password', # your MySQL password
            database='your_database'  # your DB name
        )

        if connection.is_connected():
            print("✅ Connected to MySQL Database!")
            return connection

    except Error as e:
        print(f"❌ Error while connecting to MySQL: {e}")
        return None

# Optional: test the connection
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        conn.close()



# in mysql
# CREATE DATABASE your_database;
# Then create your table:


# CREATE TABLE traffic_logs (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     timestamp DATETIME,
#     vehicle_count INT,
#     congestion_level VARCHAR(20)
# );


