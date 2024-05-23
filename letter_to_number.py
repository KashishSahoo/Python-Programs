lowers="abcdefghijklmnopqrstuvwxyz"
uppers="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def lower_number(letter):
    return lowers.index(letter)+1 if letter in lowers else None

def upper_number(letter):
    return uppers.index(letter)+1 if letter in uppers else None

t=int(input())
for i in range(t):
    a=input()

    if a.islower():
        print(lower_number(a))
    else:
        print(upper_number(a))

