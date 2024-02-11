shirs=1200
pants=1500
tshirts=600
mask=100
budget=int(input("enter your budget"))
if budget>900:
  if budget<=1000 and budget>=900:
      print("can you go for tshirts only")
  elif budget>1500 and budget>=3000:
    print("you can go pants and shirts")
  elif budget>=2000 and budget>=1500:
    print("you can go both shirts and tshirts")
  else:
    print("can you go for shirts only")
else:
  print(" sorry there is no items in your budget ")
                
            
