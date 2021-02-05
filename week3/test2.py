n = int(input("กรุณากรอกจำนวนครั้งการรับค่า : "))
result = 0
for i in range (0,n):
    num = int(input("กรอกตัวเลข : "))
    result = result + num
print ("ผลรวมค่าที่รับมาทั้งหมด = ",result)