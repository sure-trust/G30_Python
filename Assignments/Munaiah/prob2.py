budget=int(input("Enter budget of yours "))
item_prices=[200,500,450,1000]
sum=0
for i in range(0,4):
    sum=sum+item_prices[i]
print("Sum of items:",sum)
if sum<=budget:
    print("Remaining amount = ",budget-sum)
else:
    s=sum-budget
    print("Insufficient amount to purchase :",s)
    sum1=0
    for i in range(0,4):
        if s<=item_prices[i]:
            sum=sum-item_prices[i]
            break
    print("After removing the item :",sum)
