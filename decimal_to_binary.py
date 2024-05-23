t=int(input("Enter No. Of Test Cases="))
for i in range(t):
    n=int(input("Enter A Number="))
    l=[]
    while(n!=0):
        r=n%2
        l.append(r)
        n=n//2
    l=l[::-1]

    for num in l:
        print(num,end="")
    print()