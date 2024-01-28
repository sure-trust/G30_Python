N=int(input("ITEMS="))
Quantites=[1,2,3,4,5]
Prices=[8,5,7,2,6]
for i in range(0,N):
    print("ITEM:",i+1)
    print("Price=",Prices[i])
    print("Quantity=",Quantites[i])
    if Quantites[i]>3:
        print("Discount=",Prices[i]*Quantites[i]*0.15)  #15%Discount on price
        print("Total=",Prices[i]*Quantites[i]-Prices[i]*Quantites[i]*0.15)
    else:
        print("Total=",Prices[i]*Quantites[i])