t=int(input("Enter Number Of Test Cases="))
for i in range(t):
    l=[]
    inp=int(input("Enter N Value="))
    N,*values=map(int,input("Enter Numbers=").split())
    l=[N]+values
    count=0
    sum=0

    for j in l:
        if j<0:
            count+=1
            sum+=j
            
    print("The Count Of Negative Numbers=",count)
    print("The Sum Of Negative Numbers=",sum)
