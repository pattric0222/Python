import sqlite3
def insertTousers (fname,lname,ename):
    try :
        conn = sqlite3.connect(r"D:\Patrick_python\week6\example2.db")
        c = conn.cursor()
        sql = ''' INSERT INTO users (fname,lname,ename) VALUES (?,?,?) '''
        data = (fname,lname,ename)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close()

def inputdata():
    global fname,lname,ename,data1
    data2 = []
    data1 = input('input name,lastname,email : ')
    data2 = data.split(",")
    fname = data2[0]
    lname = data2[1]
    ename = data2[2]

inputdata()
insertTousers(fname,lname,ename)
