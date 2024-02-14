num=int(input("enter your range:"))
n1=0
n2=1
for n in range(0,num):
    if(n<=1):
        next=n
    else:
        next=n1+n2
        n1=n2
        n2=next
    print(next)
