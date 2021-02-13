import sqlite3
conn = sqlite3.connect (r"D:\Patrick_python\week6\example2.db")
c = conn.cursor() #crate a cusor object
c.execute('''INSERT INTO users (id,fname,lname,ename) VALUES (NULL,"A","A","A") ''')
c.execute('''INSERT INTO users VALUES (NULL,"B","B","B") ''')
conn.commit()
conn.close()