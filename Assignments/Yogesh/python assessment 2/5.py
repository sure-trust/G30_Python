char=input("enter the character:")
if len(char)==1:
    if char.isupper():
        print("entered char is uppercase")

    elif char.islower():
        print("entered char is lowercase") 

    else:
        print("it is not define ")

else:
    print("please try to enter in single charecter")               