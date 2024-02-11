budget=int(input("Enter budget to eat"))
peference=str(input("Enter veg/nonveg:"))
if budget<=1500:
    if peference=="veg":
        print("Goto Green leaf")
    else:
        print("Goto Citysquare Mall")
else:
    if peference=="nonveg":
        print("Goto ViaSouth")
    else:
        print("Goto 7thHeaven")