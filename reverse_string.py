def rev(str):
    rev_str=""
    for i in str:
        rev_str=i+rev_str
    print("Reversed String=",rev_str)
    
str=input("Enter A String=")
rev(str)