symptom1=str(input("Enter your first symptom1 (migrane,flu) : "))
symptom2=str(input("Enter your first symptom2 (dehydration,food posioning,body pains,itchy thorat) : "))
if symptom1=="migrane":
    if symptom2=="dehydration":
        print("It may be headache")
    if symptom2=="food posioning":
        print("It may be nausea")
    else:
        print("It may be increase of eye sight")
elif symptom1=="flu":
    if symptom2=="bodypains":
        print("It may be fever")
    if symptom2=="itchy thorat":
        print("It may be cough")
    else:
        print("It may be allergy")