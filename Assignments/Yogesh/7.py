fitness_level = int(input("enter your fitness level on 100 :"))

if(fitness_level>90):
    print("you need to take high calory food  and you need to have\n gym eqpuiments\n you need shoes\nyou need to run upto 5km a day")
elif(fitness_level<=90 and fitness_level>=80):
    print("you need to take average of calories and run upto 3km a day\nyou need shoes ")
elif(fitness_level<80 and fitness_level>=60):
    print("you need to take average of calories and run upto 2km a day\nyou need shoes ")
elif(fitness_level<50 and fitness_level>=30):
    print("you need to take average of calories and run upto 1km a day\nyou need shoes ")
else:
    print("you just need to jag thats all...!")
