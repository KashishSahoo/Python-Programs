n=int(input("Enter A Number=\n"))
sum=0
order=len(str(n))
num=n
while(n>0):
    r=n%10
    sum+=r**order  
    n=n//10

if(sum==num):
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not an armstrong")
