n=int(input("Enter A Number"))
print()
l=[]
count=0
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
        count+=1

print("The Factors Of Number Are...")
for j in l:
    print(j)

print()
if(count==2):
    print(f"{n} Is A Prime Number")
else:
    print(f"{n} Is Not A Prime Number")

print()
print("The Number Of Factors Are=",count)
