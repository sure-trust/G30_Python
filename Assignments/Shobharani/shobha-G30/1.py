potatos=20
qp=1
tomatos=36
qt=2
onions=100
qo=5
total_bill=potatos+tomatos+onions
quantity_total=qp+qt+qo
print("total_quantity is",quantity_total)
print("total_bill is",total_bill)
discount_onbulk =100
if total_bill>100:
    p=total_bill-discount_onbulk
    print("total payable bill  after dicount is",p)
else:
    print("not eligible")