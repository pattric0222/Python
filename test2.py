import os
list_item = ['เสื้อเชิ้ต ','เสื้อคอกลม','กางเกงขาสั้น','กางเกงขายาว','กางเกงใน']
list_price = ['100','70','50','130','20']
class mymarket :
    def menu(self):
        global choose
        print("*"*8+"Stylist shop"+"*"*8+"\t\n\tแสดงรายการสินค้า [a]\n\tเพิ่มรายการสินค้า [s]\n\tออกจากระบบ [x]\n")
        choose = input("กรุณาเลือกคำสั่ง: ")
    def showitem(self):
        print("รายการสินค้ามีดังนี้\n")
        for i in range (len(list_item)):
            print('{0: <5}{1:-<20}{2: <15}{3}'.format(i+1,list_item[i],list_price[i],"บาท"))
    def additem(self):
        while True:
            additem = input("เพิ่มรายการสินค้าหากต้องการยกเลิก กรอก exit\nเพิ่มชื่อสินค้า : ")
            if additem == 'exit':
                break
            else:
                addprice = input("เพิ่มราคาของ {} : ".format(additem))
                list_price.append(addprice)
                list_item.append(additem)
                print('ทำรายการเสร็จสิ้น')
            yesorno = input("ต้องการเพิ่มสินค้าอีกหรือไม่ (y/n): ")
            if yesorno == 'y':
                os.system('cls')
            elif yesorno == 'n':
                break

while True:
    x =  mymarket()
    x.menu()
    if choose == 'a':
        os.system('cls')
        x.showitem()
    elif choose == 's':
        os.system('cls')
        x.additem()
    elif choose =='x':
        c = input("ต้องการออกจากระบบหรือไม่ y/n: ")
        if c.lower() == 'y':
            os.system('cls')
            print("ออกจากระบบเรียบร้อยแล้ว")
            break
        elif c.lower() == 'n':
            os.system('cls')
            