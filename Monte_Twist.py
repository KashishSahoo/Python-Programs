import random
doors=[0]*3
goatdoor=[]
swap=0
dont_swap=0
j=0
while(j<5):
    x=random.randint(0,2)
    doors[x]="BWM"
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoor.append(i)
    choice=int(input("Enter your choice door number 0,1 or 2 ="))
    door_open=random.choice(goatdoor)
    while(door_open==choice):
        door_open=random.choice(goatdoor)
    
    ch=input("Goat is at Door" +str(door_open)+ " Do you wants to swap?y/n=")
    if(ch=='y'):
        if(doors[choice]=="Goat"):
            print("Player wins")
            print()
            swap=swap+1
        else:
            print("Player lost")
            print()
    else:
        if(doors[choice]=="Goat"):
            print("Player lost")
            print()
        else:
            print("Player wins")
            print()
            dont_swap=dont_swap+1
    j=j+1
print("Swapped=",swap)
print("Don't Swapped=", dont_swap)