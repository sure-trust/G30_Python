weather=input("enter('sunny'or'cold'or'rainy')")
amenities=input("enter('full amenities','some amenities','no amenities')")
print("Essential items:")
print("-tent")
print("-sleepingbag")
print("-waterbottle")
print("-food")
print("-firstaidkid")
if weather.lower()=="sunny":
  print("additional items for sunny:")
  print("-sunscreen")
  print("-sunglass")
  print("-hat")
elif weather.lower()=="rainy":
  print("additional items for rainy:")
  print("-raincoat")
  print("-tarp")
  print("-rainpants")
elif weather.lower()=="cold":
  print("additional items for cold:")
  print("-hat")
  print("-gloves")
  print("-hotwater bottle")
else:
    print("take what you want items")
if amenities.lower()=="no anemities":
  print("additional items for no anemities:")
  print("-camp stove")
  print("-cooking utensils")
  print("-towel")
elif amenities.lower()=="some amenities":
  print("additional items for some amenities")
  print("-food storage")
  print("-camp stove")
elif weather.lower()=="full amenities":
  print("additional items for full amenities:")
  print("-campstove")
  print("-waterbottle")
else:
  print("-happy journey")
  print("-have fun and enjoy the outdoors!")  


      
      
