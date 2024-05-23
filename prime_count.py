l=int(input("Enter Lower Limit="))
u=int(input("Enter Upper Limit="))
print()

print(f"The Prime Numbers In The Given Range {l} to {u}...")
print()

flag=1
count=0


for num in range(l,u+1):
    for i in range(2,num):
        if(num%i==0):
            flag=0
            break
    else:
        count=count+1
        print(num)
print()
print("The Count Of Prime Numbers Are=",count)

