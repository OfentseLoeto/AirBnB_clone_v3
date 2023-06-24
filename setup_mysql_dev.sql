#!/usr/bin/python3
import MySQLdb

def prepare_mysql_server():
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root'
    )

    # Create the database hbnb_dev_db if it doesn't exist
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS hbnb_dev_db")

    # Create the user hbnb_dev if it doesn't exist
    cursor.execute("CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'")

    # Grant all privileges on hbnb_dev_db to hbnb_dev
    cursor.execute("GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'")

    # Grant SELECT privilege on performance_schema to hbnb_dev
    cursor.execute("GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'")

    # Flush privileges to apply the changes
    cursor.execute("FLUSH PRIVILEGES")

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == '__main__':
    prepare_mysql_server()

