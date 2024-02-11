ingredients=str(input("Enter like veggies,flour,rice: "))
restrictions=str(input("Enter like on diet/no diet: "))
if ingredients=="flour":
    if restrictions!="on diet":
        print("Gulab Jamun,Cake,Laddu")
    else:
        print("Roti ,bread")
elif ingredients=="rice":
    if restrictions=="on diet":
        print("No rice")
    else:
        print("Briyani!!")
else:
    if restrictions=="on diet":
        print("Salad ,oats,juices,fruits")
    else:
        print("aloo matar,bendi masala")
