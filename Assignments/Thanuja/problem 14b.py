waste=str(input("Enter waste you need to throw : "))
if waste=="paper" or waste=="glass":
    waste_type="recyclable waste"
    disposal_method="Recycle in designated bins."
elif waste=="batteries" or waste=="chemiclas":
    waste_type="hazardous waste"
    disposal_method="Dispose of at a hazardous waste collection facility."
elif waste=="food" or waste=="yard":
    waste_type="organic waste"
    disposal_method="Compost or dispose of in green waste bins."
else:
    waste_type="non recyclable waste"
    disposal_method="Unable to determine"
print("Waste type = ",waste_type)
print("Disposal method = ",disposal_method)