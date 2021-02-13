import sqlite3
conn = sqlite3.connect (r"D:\Patrick_python\week6\work6_1.db")
c = conn.cursor() #crate a cusor object
c.execute ('''CREATE TABLE users (NO integer PRIMARY KEY AUTOINCREMENT,
    Name varchar(100) NOT NULL,
    Lastname varchar(100) NOT NULL,
    Email varchar(100) NOT NULL,
    Sex varchar(100) NOT NULL,
    Age varchar(100) NOT NULL)''')
conn.commit()
conn.close()
