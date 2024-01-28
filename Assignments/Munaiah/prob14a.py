transportation=str(input("Enter your transport like car,bike: "))
activites=float(input("Enter your distance : "))
if transportation=="car":
    if activites<=200:
        energy_usage=100
        consumption=activites*2.5+energy_usage*1.5
    else:
        energy_usage=300
        consumption=activites*3+energy_usage*2.5
if transportation=="bike":
    if activites<=250:
        energy_usage=150
        consumption=activites*1.8+energy_usage*1.5
    else:
        energy_usage=300
        consumption=activites*2+energy_usage*1.5
else:
    if activites<=280:
        energy_usage=300
        consumption=activites*2.8+energy_usage*2.5
    else:
        energy_usage=350
        consumption=activites*2.2+energy_usage*2.5
print("Carbon foot print = ",consumption)