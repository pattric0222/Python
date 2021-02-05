n = int(input("Please enter number of student : "))
print("-"*40)
listnum_student = [0,0,0,0,0,0] #list เพื่อเก็บข้อมูลจำนวนนักเรียนจากในลูป
list_score =['90-100:','80-89 :','70-79 :','60-69 :','50-59 :','0-49  :']
for i in range(0,n):    #for loop n ครั้งตามจำนวนที่ user กรอก
    score = int(input("Please enter Score : "))
    if score <=100 and score >=90 :
        listnum_student[0] += 1  # ถ้าถูกตามเงื่อนไข บวกจำนวนครั้งละ 1 คน ไปที่ listnum_student[0]
    elif score <=90 and score >=80 :
        listnum_student[1] += 1
    elif score <=80 and score >=70 :
        listnum_student[2] += 1
    elif score <=70 and score >=60 :
        listnum_student[3] += 1
    elif score <=60 and score >=50 :
        listnum_student[4] += 1
    elif score <=50 and score >=0 :
        listnum_student[5] += 1
for i in range(0,6) : # สร้าง loop print ข้อมูลจาก list
    print(list_score[i],listnum_student[i]*"*")






    

