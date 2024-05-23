print("Finding HCF Of Two Numbers...")
a=int(input("Enter 1st Number="))
b=int(input("Enter 2nd Number="))

c=min(a,b)

for i in range(c,1,-1):
    if(a%i==0 and b%i==0):
        hcf=i
        print(f"The HCF Is {hcf}")
        break