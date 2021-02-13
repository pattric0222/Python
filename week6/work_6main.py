import os           #Patrick Rusher 633055096-0
import sqlite3

word_dictionary = {}
def menu():
    global choice
    print('----ระบบลงทะเบียนเรียน----\n'+'='*25+'\n เพิ่มข้อมูลนักเรียนกด [a]\n แสดงข้อมูลนักเรียน [s]\n แก้ไขข้อมูลนักเรียน [e]\n ลบข้อมูลนักเรียน [d]\n ออกจากโปรแกรม [x]\n')
    choice = input('กรุณาเลือกทำรายการ : ')

def addstd():
    global fname,lname,ename,sex,age,data1
    data1 = input('input name,lastname,email,sex,age (do not forget ,)  : ')
    data2 = data1.split(",")
    fname = data2[0]
    lname = data2[1]
    ename = data2[2]
    sex = data2[3]
    age = data2[4]

def insertTousers (fname,lname,ename,sex,age):
    try :
        conn = sqlite3.connect(r"D:\Patrick_python\week6\work6_1.db")
        c = conn.cursor()
        sql = ''' INSERT INTO users (Name,Lastname,Email,Sex,Age) VALUES (?,?,?,?,?) '''
        data = (fname,lname,ename,sex,age)
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close()

def show():
    conn = sqlite3.connect(r"D:\Patrick_python\week6\work6_1.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    print("{0: <15}{1: <15}{2: <15}{3: <35}{4: <15}{5: <15}\n".format('ลำดับที่','ชื่อ','นามสกุล','อีเมลล์','เพศ','อายุ')+"-"*120)
    for i in rows:
        print("{0: <10}{1: <15}{2: <14}{3: <33}{4: <15}{5: <15}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    print('ทำการแสดงรายการเสร็จสิ้น\n')

def editstdinfo(fname,lname,ename,sex,age,change): 
    try :
        conn = sqlite3.connect(r"D:\Patrick_python\week6\work6_1.db")
        c = conn.cursor()
        data = (fname,lname,ename,sex,age,change)
        c.execute('''UPDATE users SET Name =?,Lastname =?,Email =?,Sex =?,Age =? WHERE NO = ?''',data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to edit : ',e)
    finally :
        if conn :
            conn.close()
    
def deletestd(delete):
    try :
        conn = sqlite3.connect(r"D:\Patrick_python\week6\work6_1.db")
        c = conn.cursor()
        c.execute(''' DELETE FROM users WHERE NO = ?''',delete)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to delete : ',e)
    finally :
        if conn :
            conn.close()

while True:
    menu()
    if choice == 'a':
        os.system('cls')
        addstd()
        insertTousers(fname,lname,ename,sex,age)
    elif choice =='s':
        os.system('cls')
        show()
    elif choice =='e':
        os.system('cls')
        change = input('กรอกตำแหน่ง (ตัวเลข) ที่ต้องการแก้ไขข้อมูล กรอก 0 หากไม่ต้องการแก้ไขข้อมูล : ')
        if change != '0':
            addstd()
            editstdinfo(fname,lname,ename,sex,age,change)
    elif choice =='d':
        os.system('cls')
        delete = input('กรอกตำแหน่ง (ตัวเลข) ที่ต้องการลบข้อมูล กรอก 0 หากไม่ต้องการลบข้อมูล : ')
        if delete != '0':
            deletestd(delete)
    elif choice =='x':
        os.system('cls')
        c = input("ต้องการออกจากโปรแกรมใช่หรือไม่ y/n: ")
        if c.lower() == 'y':
            os.system('cls')
            break
        elif c.lower() == 'n':
            os.system('cls')
    
    '''input เพิ่มจำนวนนักเรียน
    Panadda,Butmala,panaddaaa@gmail.com,female,16
    Patrick,Rusher,patrickrusher@kkumail.com,male,12
    Marcus,Rashford,rashford@hotmail.com,male,15 '''