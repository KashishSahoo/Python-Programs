def fibo(n):
    a,b=0,1

    if(n==1):
        return(a)
    elif(n==2):
        return(b)
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return(b) #0,1,1,2,3,5,8
t=int(input("Enter n Value="))
for i in range(t):
    n=int(input("To Find nth Fibonacci="))
    r=fibo(n)
    print(r)