lower=int(input("Enter Starting Number="))
upper=int(input("Enter Ending Number="))

for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        r=temp%10
        sum+=r**order
        temp=temp//10
    if num==sum:
        print(num)
