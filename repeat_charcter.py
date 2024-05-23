t=int(input("Enter N Value="))

for j in range(t):
    s=input("Enter A String=")
    ch=input("Enter Character=")
    r=0

    for i in range(len(s)):
        if(s[i]==ch):
            r=r+1
    print(r)
