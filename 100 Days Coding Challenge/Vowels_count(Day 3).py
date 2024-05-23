def count(s):
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    
    for i in s:
        if(i=='a'):
            c1+=1
        elif(i=='e'):
            c2+=1
        elif(i=='i'):
            c3+=1
        elif(i=='o'):
            c4+=1
        elif(i=='u'):
            c5+=1

    print(f"a:{c1}")
    print(f"e:{c2}")
    print(f"i:{c3}")
    print(f"o:{c4}")
    print(f"u:{c5}")

t=int(input("Enter Number Of Test Cases="))
for i in range(t):
    str=input("Enter A String=")
    count(str)