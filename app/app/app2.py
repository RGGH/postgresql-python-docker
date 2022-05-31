"""

"""
import os
from db_con import dbConnection

# Test of reading params from file
db = dbConnection()

# Test of version of the database
db.db_version()

# Test of inserting data to users table
db.execute("INSERT INTO users (name, user_id) VALUES ('ABC', 106)")

db.commit()

# Test of SELECT query
rows = db.fetchall("SELECT * FROM users")
for row in rows:
    print(row)

db.close()