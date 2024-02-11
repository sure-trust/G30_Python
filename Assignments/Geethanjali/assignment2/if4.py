chips=100
jam=200
chocolate=150
biscuit=250
totalprice=int(input("enter your price:"))
if totalprice>=3000 and totalprice<=4000:
    print("you won a discount=20%")
elif totalprice>=4000 and totalprice>=5000:
      print("you won a discount=30%")
else:
    print("vist again!")
discount=int(input("enter your discount"))
dprice=discount/100
discountprice=totalprice/dprice
payableprice=totalprice-discountprice
print("payableprice",payableprice)


























