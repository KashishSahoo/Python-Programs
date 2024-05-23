import math 
def min(a,n):
    m=0
    a=0

    for t in a:
        r=math.ceil(t/2)
        a+=r
    return a

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    print(min(n,a))