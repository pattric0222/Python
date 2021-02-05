def inputinfo():
        global hello,info,name,lastname,sex,year,department,hometown
        print("-"*30+"แนะนำตัว"+"-"*40)
        info = input("ชื่อ:นามสกุล:เพศ:ชั้นปีที่ศึกษา:สาขาวิชา:จังหวัดภูมิลำเนา ==>")
        allinfo = info.split(":")
        name = allinfo[0]
        lastname = allinfo[1]
        sex = allinfo[2]
        year = allinfo[3]
        department = allinfo[4]
        hometown = allinfo[5]
        if (sex == "ชาย"):
            hello = 'สวัสดีครับ'
        elif (sex == 'หญิง'):
            hello = 'สวัสดีค่ะ'
class nisit : 
    def __init__(self,name,lastname,sex,year,department,hometown):
        self.name = name
        self.lastname = lastname
        self.sex = sex
        self.year = year
        self.department = department
        self.hometown = hometown
    def showinfo(self):
        print(hello,self.name,self.lastname,self.sex,self.year,self.department,self.hometown)

inputinfo()
x = nisit(name,lastname,sex,year,department,hometown)
x.showinfo()


    
