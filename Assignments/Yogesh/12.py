assignment = float(input("enter your assignment marks for 10:"))

exams = float(input("enter you exam marks for 100:"))

attendence = float(input("enter your attendece in precentage:"))

if assignment==10:
    assign = 2
elif (assignment<10 and assignment>8):
    assign = 1.5
elif(assignment>5 and assignment<8):
    assign = 1
else:
    assign = 0
   
   
if (exams>90 ):
    exam = 4
elif (exams<=90 and exams>=70):
    exam = 3
elif(exams<70 and exams>=50):
    exam = 2.5
elif(exams<50 and exams>40):
    exam = 2
else:
    exam =0
if(attendence>80):
    attend = 4
elif(attendence>60 and attendence<80):
    attend = 3
elif(attendence>40 and attendence<60):
    attend = 2
else:
    attend = 0
    
total_credits = 9
gained_credits = assign+exam+attend

grade = gained_credits/total_credits*10

print(grade)
    
    
    
    
