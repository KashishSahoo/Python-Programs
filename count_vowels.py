t=int(input("Enter N Value="))

for i in range(t):
    lis=[]
    count=0
    n=input("Enter A String=")
    l=len(n)

    for j in n:
        lis.append(j)
    for k in range(l):
        if(lis[k]=='a' or lis[k]=='e'or lis[k]=='i' or lis[k]=='o'or
           lis[k]=='u' or lis[k]=='A'or lis[k]=='E' or lis[k]=='I' or lis[k]=='O' or lis[k]=='U'):
            count+=1
    print("The Number Of Vowels Are=",count)
    