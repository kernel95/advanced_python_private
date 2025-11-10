# database_intro.py

import sqlite3
from Member import members
conn = sqlite3.connect("member_database_trainer.db")

cursor = conn.cursor()

# sql = """
# CREATE TABLE IF NOT EXISTS members (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT UNIQUE NOT NULL,
#     active BOOLEAN NOT NULL
# );
# """
# cursor.execute(sql)


# sql = "INSERT INTO members (name, email, active) VALUES ('Alice', 'alice@gmail.com', 1)"
# cursor.execute(sql)
# sql = "INSERT INTO members (name, email, active) VALUES ('Carol', 'Carol@gmail.com', 1)"
# cursor.execute(sql)
# sql = "INSERT INTO members (name, email, active) VALUES ('Diana', 'Diana@gmail.com', 1)"
# cursor.execute(sql)

sql = "SELECT * FROM members"
rs = cursor.execute(sql)
for row in rs: 
    print(row)

conn.commit()
conn.close()