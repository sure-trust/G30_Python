budget=int(input("Enter budget to eat"))
peference=str(input("Enter veg/nonveg:"))
if budget<=500:
    if peference=="veg":
        print("Goto arunodhaya")
    else:
        print("Goto jyotji Mall")
else:
    if peference=="nonveg":
        print("Goto ViaSouth")
    else:
        print("Goto Lucky9")
