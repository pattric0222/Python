import datetime
num_people = int(input('Enter number of competitor : '))
list_name ,list_score ,list_time ,list_hit  =[], [], [], []
for i in range (num_people) :
    info = input("Please enter (name,score,time) => ")
    splitinfo = info.split(",")
    list_name.append(splitinfo[0])
    list_score.append(splitinfo[1])
    list_time.append(splitinfo[2])
    list_hit.append(float(list_score[i])/float(list_time[i]))

date =  datetime.datetime.now()
datenew = date.strftime('%G-%m-%d %H:%M:%S')
print('\nShotgun ',date.strftime('%A'),' Training ',date.strftime('%Y'))
print(datenew)
print(""+"-"*120+"\n{0:-<8}{1:-<13}{2:-<12}{3:-<20}{4:-<15}{5:-<20}{6}".format('No.','Points','TIME','CompetitorName','Hit factor','State Points','State Percents\n'+"-"*120))
for k in range (num_people):
    j = k
    for j in range(num_people):
        if list_hit[k] > list_hit[j]:
            z,x,c,v = list_hit[k],list_name[k],list_score[k],list_time[k]
            list_hit[k],list_name[k],list_score[k],list_time[k] = list_hit[j],list_name[j],list_score[j],list_time[j]
            list_hit[j],list_name[j],list_score[j],list_time[j] = z,x,c,v

for i in range (num_people):
    stage_pt = (((list_hit[i])/(max(list_hit)))*50) 
    stage_per = (stage_pt/((max(list_hit)/(max(list_hit)))*50))*100
    print("{0: <8}{1: <13}{2: <12}{3: <20}{4: <15}{5: <20}{6}".format(i+1,list_score[i],list_time[i],list_name[i],'%.4f'%list_hit[i],'%.4f'%stage_pt,'%.2f'%stage_per))
