goal_amount=100000;
goal_time = 200
perday_savings=int(input("your savings per day:"))
previous_money = 20000
current_money = previous_money+perday_savings
print("your current money is: ")
print(current_money)
days = goal_amount/perday_savings
if(days==goal_time):
    print("your saving enough money per day...!")
elif(days>goal_time):
    print("your saving not enough money to achive in your deadline...!")
else:
    print("your saving more money than enough...! ")    


'''if  perday_savings>1000:
    print("you are earning enough money to reach your goal aim")
    
elif perday_savings>800 and perday_savings<1000:
    print("you have earning some what enough money to reach the goal aim")
    
elif perday_savings>600 and perday_savings<800:
    print("you want save some more money per day to reach your goal aim")  '''
  
