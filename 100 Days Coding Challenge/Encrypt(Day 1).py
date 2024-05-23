alpha=['a','b','c','d','e','f','g','h','i','j','k','l',
       'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(str,key):
    cipher=""
    for char in str:
        pos=alpha.index(char)
        n=(pos+key)%26
        cipher+=alpha[n]
    print("The Cipher Text Is=",cipher)

t=int(input("Enter Number Of Test Cases="))
for i in range(t):
    s,k=map(int,input("Enter Length Of String And Shift Key=").split())
    st=input("Enter String=").lower()
    encrypt(st,k)