import mysql.connector

# Connect to MySQL Server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Manan@1234"
)

cursor = db.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")

# Select database
cursor.execute("USE student_db")

# Create students table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        course VARCHAR(100) NOT NULL,
        city VARCHAR(100) NOT NULL
    )
""")

print("Database and table created successfully")

db.close()