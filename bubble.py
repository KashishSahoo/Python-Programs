# 5,1,4,2,8
# 1,5,4,2,8
# 1,4,5,2,8
# 1,4,2,5,8

# 1,4,2,5,8
# 1,2,4,5,8

def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
a=[7,99,1,2,44,89]
bubble(a)

for i in a:
    print(i)

