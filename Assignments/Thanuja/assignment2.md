 **if -else**

 **1.Even or Odd**

 **Sol:**

 n=int(input("Enter a number : "))

 if(n%2==0):

    print(n,"is even number")

 else:

    print(n,"is odd number")

 **Output:**

 Enter a number : 5

 5 is odd number

 Enter a number : 4

 4 is even number
 
 **2.Eligibility for vote**

 **Sol:**
 age=int(input("Enter age : "))

 if(age>=18):

    print("Eligible for vote")

 else:

    print("Not Eligible for vote under 18")

 **Output:**

 Enter age : 23

 Eligible for vote

 Enter age : 15

 Not Eligible for vote under 18

 **3.Leap Year**

 **Sol:**
 
 year=int(input("Enter year : "))

 if((year%4==0) and ( year%400==0  or  year%100!=0) ):

	print(" leap year")

 else:

	print(" not Leap year")

 **Output:**

 Enter year : 2000

 leap year

 Enter year : 1997

 not Leap year

 Enter year : 1400

 not Leap year

 Enter year : 2024

 leap year

 **4.Discount**

 **Sol:**

 price=float(input("Enter price of product : "))

 discount=float(input("Enter discount in percent :"))

 if(price>=200):

    amount_paid=price-((price*discount)/100)

 else :

    amount_paid=price
    
 print("Total amount to be paid = ",amount_paid)

 **OUTPUT**

 Enter price of product : 25

 Enter discount in percent :1

 Total amount to be paid =  25.0

 Enter price of product : 3000

 Enter discount in percent :2

 Total amount to be paid =  2940.0

 **5.Upper case or Lower Case**

 **Sol:**

 ch=(input("Enter a character : "))

 if(ch.isupper()):

    print("Entered character is in uppercase")

 elif(ch.islower()):

    print("Entered character is in lowerrcase")

 else:

       print("Entered character is not in uppercase or lowercase")

 **OUTPUT:**

 Enter a character : a

 Entered character is in lowerrcase

 Enter a character : D

 Entered character is in uppercase

 Enter a character : %

 Entered character is not in uppercase or lowercase

 **6.Positive or Negative Or Zero**

 **Sol:**

 num=int(input("Enter a number : "))

 if(num>0):

    print("Positive number")

 elif(num<0):

    print("Negative number")

 else :

    print("Zero")

 **Output:**

 Enter a number : 23

 Positive number

 Enter a number : 0

 Zero

 Enter a number : -12
 
 Negative number


 











