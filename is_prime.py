num=int(input("Enter A Number="))
flag=False

if num==1:
    print(num,"Is Not A Prime Number")
elif num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
    if flag:
        print(num,"Is Not A Prime Number")
    else:
        print(num,"Is A Prime Number")
