#!/usr/bin/python3

import MySQLdb

conn = MySQLdb.connect(host='localhost', user=hbnb_test, passwd=hbnb_test_passwd)

cursor = conn.cursor()
db_query = "CREATE DATABASE IF NOT EXISTS hbnb_test_db"
cursor.execute(db_query)

user_query = "CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_passwd'"
cursor.execute(user_query)

grant_privileges = "GRANT ALL PRIVILEGES hbnb_test_db.* TO 'hbnb_test'@'localhost'"
cursor.execute(grant_privileges)

grant_select = "GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'"
cursor.execute(grant_select)

flush_query = "PRIVILEGES"
cursor.execute(flush_query)

cursor.close()
conn.close()
