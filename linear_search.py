def linear(n,x):
    e=[]
    for i in range(0,n+1):
        e.append(i)
    flag=0
    count=0
    for i in e:
        count+=1
        if(i==x):
           print("Yes!!I Found My number ")
           print(f"At postion{i}")
           flag=1
           break
    if(flag==0):
        print("Number Not Found")
    print(f"Number Of Iterations{count}")

linear(50,25)

        