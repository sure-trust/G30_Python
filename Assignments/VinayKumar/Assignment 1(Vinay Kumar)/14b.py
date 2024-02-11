waste = str(input("enter the wastage you need throw: "))
if waste =="paper" or waste=="glass":
   waste_type = "recyclable waste"
   disposal_waste="recycle in designated bins"

elif waste=="batteries" or waste=="chemicals":
    waste_type="hazardous waste"
    disposal_method="dispose of at a hazardous waste collection facility."
    
elif waste=="food" or waste=="yard":
    waste_type="organic waste"
    disposal_method="compost or dispose of in green wasre bins."
    
else:
    waste_type="non recyclable waste"
    disposal_method="uable to detmine"

print ("waste_type=",waste_type)    
print ("disposal method=",disposal_method)        
  
    
