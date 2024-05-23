print("All Prime Number In Given Interval..")
l=int(input("Enter Lower Limit="))
u=int(input("Enter Upper Limit="))

for num in range(l,u+1):
    flag=0
    for i in range(2,num):
        if(num%i==0):
            flag=1
            break
    if(flag==0):
        print(num)