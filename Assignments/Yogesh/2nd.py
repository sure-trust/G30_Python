budget = int(input("enter the alloted budget :"))
jeans = 300
shirt = 260
t_shirt = 150
shorts = 250
tp = jeans + shirt+t_shirt+shorts
if budget>150 and budget<200 :
    print("you can buy only t_shirts...!")
elif (budget>200 and budget<500):
    print("you can buy shorts and t_shirts")
    
elif(budget>500 and budget<1000):
    print("you can buy shirts,t_shirts,jeans,short") 
elif(budget>=1000):
    print("you can buy anything") 
else:
    print("you can't buy anything....!")