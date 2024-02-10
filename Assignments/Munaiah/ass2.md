**if-else loops**

**1.PROGRAM:**

n=int(input('enter n value='))

print('given number is',n)

r=n%2

if (r==0):

    print(n,"is an even number")

else:

     print(n,"is an odd number")
    
**OUTPUT:**

enter n value=5

given number is 5

5 is an odd number

**2.PROGRAM:**

age=int(input("enter the age="))

if age>18:

    print("you are eligible for voting")

else:

    print("you are not eligible for voting")

**OUTPUT:**

enter the age=5

you are not eligible for voting

enter the age=20

you are eligible for voting

**3.PROGRAM:**

N=int(input("YEAR="))

R=N%4

if (R==0):

    print(N,"IS A LEAP YEAR")

else:

    print(N,"IS NOT A LEAP YEAR")

**OUTPUT:**

YEAR=2024

2024 IS A LEAP YEAR

YEAR=2025

2025 IS NOT A LEAP YEAR


**4.PROGRAM:**

N=float(input("COST OF THE PRODUCT="))

D=float(input("DISCOUNT IN PERCENTAGE="))

if N>=499:

    M=(D/100)*N

    print("TOTAL COST OF THE PRODUCT=",N-M)

else:

    print("TOTAL COST OF THE PRODUCT=",N)

**OUTPUT:**

COST OF THE PRODUCT=500

DISCOUNT IN PERCENTAGE=10

TOTAL COST OF THE PRODUCT= 450.0


**5.PROGRAM:**

character=input("enter a character")

if character.isupper():

    print("THE CHARACTER IS UPPER CASE")

elif character.islower():

     print("THE CHARACTER IS LOWER CASE")

else:

    print("NOT UPPER NOT LOWER CASES")

**OUTPUT:**

enter a character M

THE CHARACTER IS UPPER CASE


enter a characterm

THE CHARACTER IS LOWER CASE


**6.PROGRAM:**

NUMBER=int(input("NUMBER="))

if NUMBER>0:

    print(NUMBER,"IS POSITIVE NUMBER")

else:

    print(NUMBER,"IS NEGATIVE NUMBER")


**OUTPUT:**

NUMBER=10

10 IS POSITIVE NUMBER

NUMBER=-10

-10 IS NEGATIVE NUMBER

 