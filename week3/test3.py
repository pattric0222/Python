print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม")
favfoodlist = []
n = 0
while(True) :
    n += 1
    fav = input("อาหารโปรดอันดับที่ {} คือ \t".format(n))
    favfoodlist.append(fav)
    if fav == 'exit':
        break
print("อาหารโปรดของคุณมีดังนี้ ",end= "")
for x in range (1,n):
        print(x,".",favfoodlist[x-1],end="  ")