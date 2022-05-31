"""
Example of use 
"""
import os
from db_con import dbConnection

# Test of reading params from file
db = dbConnection()

# Test of version of the database
db.db_version()

# Test of executing CREATE TABLE query
db.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, f_name VARCHAR(16) NOT NULL, l_name VARCHAR(32) NOT NULL) ")
db.commit()

# Test of inserting data to users table
db.execute("INSERT INTO users (f_name, l_name) VALUES ('John', 'Doe')")
db.execute("INSERT INTO users (f_name, l_name) VALUES ('Anna', 'Green')")
db.commit()

# Test of SELECT query
rows = db.fetchall("SELECT * FROM users")
for row in rows:
    print(row)

# Test of counting rows query
row = db.fetchone("SELECT COUNT(*) FROM users")
print("Num of records: ", row[0])

# Test of copy of the table to csv file
db.copy_to('users.csv', 'users', ':' )

# Test of copy records from file to new table
db.execute("CREATE TABLE IF NOT EXISTS new_users (id SERIAL PRIMARY KEY, f_name VARCHAR(16), l_name VARCHAR(32))")
db.commit()
db.copy_from('users.csv', 'new_users', ':' )
rows = db.fetchall("SELECT * FROM new_users")
for row in rows:
    print(row)
    
# Test of deleting tables
db.execute("DROP TABLE users")
db.commit()
db.execute("DROP TABLE new_users")
db.commit()

# Closing a connection
db.close()