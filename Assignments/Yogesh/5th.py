budget =  int(input("enter the budget:"))
preference = str((input("enter your preference:among this 1.Biryani,2.veg_biryani,3.roti in small letters :")))

if(preference=="biryani" ):
    if(budget>=300):
        print("you can go to the hotel taj")
    else:
        print("you cant go restuarent")
elif(preference=="veg biryani"):
    if(budget>=250):
        print("you have to go the hotel bans")
    else:
        print("in this price you cant go in to restuarent")
elif(preference=="roti"):
    if(budget>=150):
        print("you can go the hotel viharii")
    else:
        print("in this price you cant go in to restuarent")
else:
    print("your required food is not availble in this region :")

        
    


    




'''if budget>1000 and budget<1500:
    print("you can go into hotel taj")
elif budget>100 and budget<1000:
    print("you can go into hotel bans")    
else:
    print("you cannot enter into any restaurants")'''
    