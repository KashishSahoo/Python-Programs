n=int(input("Enter Number Of Terms="))
a=0
b=1
print(a)
print(b)
n=n-2
for i in range(1,n):
    c=a+b
    print(c)
    a=b
    b=c