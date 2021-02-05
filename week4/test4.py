import os
word_dictionary = {}
def menu():
    global choice
    print("-"*40+'\nพจนานุกรม\n 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์ทั้งหมด\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n'+"-"*40)
    choice = input('Input Choice : ')

def adddict():
    word = input("\nเพิ่มคำศัพท์ :\t")
    typeword = input("ชนิดของคำ(n. , v. , adj. , adv.): ")
    mean = input("ความหมาย :  ")
    word_dictionary[word] = typeword+mean
    print("เพิ่มคำศัพท์เรียบร้อยแล้ว ")

def showdict():
    print("\n\tคำศัพท์ทั้งหมด\n{0: <11}{1: <8}{2}".format('คำศัพท์','ประเภท','ความหมาย'))
    for key in word_dictionary:
        print("{}{:<3}{}".format(key,'',word_dictionary[key]))

def deletee():
    delete_word = input("\nพิมพ์คำศัพท์ที่ต้องการลบ: ")
    yes_no = input("ต้องการลบ {} ใช่หรือไม่ (y/n): ".format(delete_word))
    if yes_no == 'y':
        del word_dictionary[delete_word]
        print("ลบ "+delete_word+" เรียบร้อยแล้ว")
while True:
    menu()
    if choice == '1':
        adddict()
    elif choice =='2':
        showdict()
    elif choice =='3':
        deletee()
    elif choice =='4':
        c = input("ต้องการใช้งานโปรแกรมต่อหรือไม่ y/n: ")
        if c.lower() == 'y':
            os.system('cls')
        elif c.lower() == 'n':
            os.system('cls')
            break

"""Ekkata,50,14.34
Pongpol,50,11.72
Bank,0,20.31
Punlop,50,18.62
Phatpitcha,50,18.60
Wiwat,50,14.57
Apichet,50,15
Srisakul,50,18.22
Anunath,50,19.73
Prapat,40,39.31
Natee,50,19.80
Thossapoom,50,21.57
Nattapong,40,17.34
Vorapol,50,22.68
Jakgrapat,50,23.90
Sanya,50,14.76
Krisana,50,16.81
Natakorn,50,16.87
Siraphak,50,17.03
Chainarong,50,26.49
Kritsanaluk,50,14.48
Dhapanon,48,14.07"""