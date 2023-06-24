#!/usr/bin/pytho3
import MySQLdb

'''Connect to the MySQL server'''

db = MySQLdb.connect("user=hbnb_test, passwd=hbnb_test_pwd, host='localhost', port=3306")

'''Create a cursor object to execute SQL queries'''
cursor = db.cursor()

'''Create the hbnb_test_db database if it doesnt exist'''
db_query = "CREATE DATABASE IF NOT EXISTS hbnb_test_db"
cursor.execute(db_query)

'''Create the hbnb_test user with the specified password'''
user_query = "CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd'"
cursor.execute(user_query)

'''Grant all privileges to hbnb_test on the hbnb_test_db database'''
grant_privileges = "GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost'"
cursor.execute(grant_privileges)

'''Grant select on performance_schema'''
grant_select = "GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'"
cursor.execute(grant_select)

'''Flush privileges to apply the changes'''
flush_query = "FLUSH PRIVILEGES"
cursor.execute(flush_query)

'''Close the cursor and database connection'''
cursor.close()
db.close()
