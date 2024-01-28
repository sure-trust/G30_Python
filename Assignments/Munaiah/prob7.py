fitness_level=str(input("Enter fitness level(beginner/intermediate/advanced"))
if fitness_level=="beginner":
    print("No equipment needed")
    print("walking,push-ups")
elif fitness_level=="intermediate":
    print("Running,skipping,dumb bells,planks")
    equipment="Treadmill,Skipping ropes,Dumb bells,Yoga mat"
else:
    print("Dead lifts,pull ups,dips,squat,lunge")
    equipment="bar bell,lifts,leg press machine,battle ropes,boxing machine"
print(equipment)