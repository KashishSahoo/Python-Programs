def count(lst):
    lst.sort(reverse=True)

    c1=[]
    c2=[]
    c3=[]

    c=0

    while lst:
        if c==0:
            c1.append(lst.pop(0))
        elif c==1:
            c2.append(lst.pop(0))
        else:
            c3.append(lst.pop(0))
        c=(c+1)%3
    print("Alpha:",sum(c1))
    print("Beta:",sum(c2))
    print("Gamma:",sum(c3))

t=int(input("Enter No. Test Cases="))
for i in range(t):
    li=[]
    n=int(input("Enter Number Of Coins="))
    N,*values=map(int,input("Coin Values=").split())
    li=[N]+values
    count(li)
