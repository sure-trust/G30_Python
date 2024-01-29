tomoto = int(input("enter the purchased price of the tomotos: "))
soup = int(input("enter the purchased price of the soups: "))
books = int(input("enter the purchased price of the books: "))
tp = tomoto+soup+books
print("total price without discount")
print(tp)
#tp = int(input("enter the total price: "))
if tp<1000:
    print("no discount available")
    

elif (tp>1000)and (tp<1500) :
    dis = tp* 0.05
    tp = tp-dis
    print("total price with discount :")
else:
    dis = tp*0.07
    tp = tp-dis  
    print("total price with discount :")

print(tp)

