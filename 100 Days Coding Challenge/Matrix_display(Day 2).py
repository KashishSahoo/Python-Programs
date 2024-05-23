def matrix(n,m):
    num=1

    for i in range(n):
        for j in range(m):
            if(num%5==0):
                print("(BUS)",end=" ")
                num+=1
            else:
                print(f"({num})",end="   ")
                num+=1
        print()
t=int(input("Enter Number Of Test Cases="))
for i in range(t):
    n,m=map(int,input("Enter Number Of Rows And Columns=").split())
    matrix(n,m)