listinfo = []
while(True) :
    print("\n\n--------แพทริค Mart------------\nเพิ่ม [a]\nแสดง [s]\nออกจากระบบ [x]")
    type_pick = input(" ")
    if type_pick == 'a' :
        info = (input("ป้อนรายการลูกค้า(รหัส:ชื่อ:จังหวัด)"))
        listinfo.append(info)
        print("\n******ข้อมูลได้เข้าสู่ระบบแล้ว*******\n")
    elif type_pick == 's' :
        print("{0:-<30}".format(""))
        print("{0:-<13}{1:-<13}{2}".format('รหัส','ชื่อ','จังหวัด'))
        print("{0:-<30}".format(""))
        for i in listinfo:
            listinfo_full = i.split(":")
            print('{}'.format(listinfo_full))
    elif type_pick == 'x' :
        c = input("ต้องการปิดโปรแกรมใช่หรือไม่ y/n: ")
        if c == 'n':
            print('ทำคำสั่งถัดไป')
        elif c == 'y':
            print('จบการทำงาน')
            break
