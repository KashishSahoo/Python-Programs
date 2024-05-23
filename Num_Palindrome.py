n=int(input("Enter An Number="))
temp=n
rev=0

while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10

if(temp==rev):
    print("Number Is A Palindrome")
else:
    print("Number Is Not  A Palindrome")