weather=str(input("Enter weather (hot,cold)"))
amenities=str(input("Enter amentities (Trecking,fishing,campfire)"))
if weather=="hot":
    if amenities=="trecking":
        print("Get climbing equipments,water bottle,loose clothes,hat,sunglasses")
    elif(amenities=="fishing"):
        print("Get fishing equipments,water bottle,loose clothes,hat,sunglasses,barbecque")
    else:
        print("Get water bottle,loose clothes,hat,sunglasses")
else:
    if amenities=="campfire":
        print("Get sweater,raincoats and equipment for campfire like matchbox ")
    else:
        print("Get heater ,sweater")