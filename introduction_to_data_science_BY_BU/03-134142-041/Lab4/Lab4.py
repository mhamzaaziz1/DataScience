#LAB 4 task 1:

count = 0
num = 1
sum = 0
while num != 0:
    num=int(input("enter the number:"))
    count += 1
    sum = sum + num

if count !=0:
    print ("sum of values are:",sum)
    count -= 1
    print("Avg:",sum/count)        
else:
    print(count)

        

#LAb 4 task 2:
val1 = int(input(" enter for horizontal values"))
val2 = int(input(" enter for vertical values"))
char1 = '@'
for row in range(val1):
    for col in range(val2):
        print(char1)
    print()    
        

