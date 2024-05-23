def binary(a,x):
    f=0
    l=len(a)-1
    flag=0   # flag=0 means that the element has been not found yet
    

    while(f<=l and flag==0):
        mid=(f+l)//2

        if(x==a[mid]):
            flag=1
            print(f"The Element Is At Location={mid+1}")
            return
        else:
            if(x<a[mid]):
                l=mid-1
            else:
                f=mid+1
    print("The Element Is Not Found")

a=[9,89,55,80,99,100]
binary(a,99)        