skills=str(input("Enter your skills(coding,reasearch) :"))
interests=str(input("Enter your interests(programming,reading) : "))
trends=0
if skills=="coding":
    if interests=="programming":
        trends=8
    if interests=="logic":
        trends=10
if skills=="research":
    if interests=="reading":
        trends=9
if trends<=5:
    print("Trends = ",trends)
    print("Not eligilble for college major")
else:
    print("Trends = ",trends)
    print("Eligible for college major")