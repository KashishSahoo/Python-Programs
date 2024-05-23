import random
year=random.randint(1900,2024)
print(year)
if(year%4==0 and year%100!=0 or year%400==0):
    print("Leap Year")
else:
    print("Not Leap Year")