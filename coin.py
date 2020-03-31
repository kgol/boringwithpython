import random
numberOfStreaks = 0
numberOfStreaksT = 0
list=[]
streakH = 0
streakT = 0
for experimentNumber in range(10):
    for i in range(10):
        x=random.randint(0,1)
        if x==0:
            list.append('H')
        elif x==1:
            list.append('T')

for item in list:
        if item=='H':
            streakH +=1
            streakT =0
            if streakH == 6:
                numberOfStreaks +=1
        elif item =='T':
            streakT +=1
            streakH =0
            if streakT == 6:
                numberOfStreaks +=1
    






H = ('H','H')
T = ('T','T','T','T','T','T')
#numberOfStreaksH = list.count(('H','H'))
#numberOfStreaksT = list.count(T)
print(list)
print(numberOfStreaks)
print(numberOfStreaksT)

