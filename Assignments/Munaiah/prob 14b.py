waste=str(input("Enter waste to throw : "))
if waste=="paper" or waste=="glass" or waste=="metals":
    waste_type="recyclable waste"
    disposal_method="Recycle in designated bins."
elif waste=="batteries" or waste=="chemiclas" or waste=="scrap":
    waste_type="hazardous waste"
    disposal_method="Dispose of at a hazardous waste collection facility."
elif waste=="food" or waste=="dung":
    waste_type="organic waste"
    disposal_method="Compost or dispose of in green waste bins."
else:
    waste_type="non recyclable waste"
    disposal_method="Unable to determine disposal method"
print("Waste type = ",waste_type)
print("Disposal method = ",disposal_method)