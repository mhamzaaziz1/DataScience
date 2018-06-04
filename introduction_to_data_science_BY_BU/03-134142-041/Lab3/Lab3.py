#Task:1
Afridi = ('Afridi', 10)
Aamir = ('Aamir', 1)
Babar = ('Babar', 3)
Imad = ('Imad' , 6)
KarachiKing = {}
KarachiKing [Afridi] =1
KarachiKing [Aamir] =2
KarachiKing [Babar] =3
KarachiKing [Imad] =4
print('Players are :')
for Players in KarachiKing:
    print (Players)

#Task:2
Mills = ("Mills", 7)
Hassan = ("Hassan", 9)
Babar = ("Babar", 3)
Imad = ("Imad", 4)
Afridi = ("Afridi", 10)
Aamir = ("Aamir", 1)

KarachiKings = {Afridi: 1, Aamir: 2, Babar: 3, Imad: 4}
maxi = 0
temp = 0
for variable, a in KarachiKings:
    if (a> maxi):
        maxi = a
print (maxi)
print (len(KarachiKings))
print (Aamir in KarachiKings)

#Task:3
k = 1
for i in range(0, 5):
   for j in range(0, k):
      print("* ", end="")
   k = k + 2
   print()
k = 7
for i in range(0, 5):
   for j in range(0, k):
      print("* ", end="")
   k = k - 2
   print()




#Task:4
#//Letter H
result_str="";
Hamza="";    
for Row in range(0,25):    
    for Col in range(0,25):     
        if ((Col == 1 or Col == 24) or (Row == 12 and Col > 1 and Col < 25)):  
            Hamza=Hamza+"*"    
        else:      
            Hamza=Hamza+" "    
    Hamza=Hamza+"\n"    
print(Hamza);    



