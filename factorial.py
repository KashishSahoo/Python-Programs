fact=1
num=int(input("Enter A Number="))

if num<0:
    print("No Factorial For Negative Numbers")
elif num==0:
    print("Factorial Of 0 Is One")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(f"The Factorial Of {num} Is {fact}")