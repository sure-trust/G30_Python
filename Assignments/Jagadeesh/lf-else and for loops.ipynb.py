
'''1. **Print a pattern**: Write a Python program to print the following pattern using nested loops:
   ```
   *
   **
   ***
   ****
   *****'''
n = int(input('enter the num:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='' )
    print()

#Write a Python program that prints the multiplication table (from 1 to 10) using nested loops.
n = int(input('enter the num:'))
for i in range(1,n+1):
    for j in range(1,10+1):
        print(i,'X' , j ,'=' ,i*j)
    print()

#Write a Python program using nested loops to find all prime numbers within a given range.
n = int(input('enter the number:'))
for i in range(2,n+1):
    ind = True
    for j in range(2,i):
        if i % j == 0:
            ind = False
    if ind == True:
        print(i)

#Write a Python program to print the Fibonacci sequence's first `n` numbers using a loop within a loop.
n = int(input('enter the number:'))
a = 0
b = 1
while b <= n:
    c = a+b
    print(b)
    a = b
    b = c

#2. Write a program that takes a person's age as input and determines if they are eligible to vote using an if-else statement.
age = int(input('enter your age:'))
if age >= 18:15
    print('you are eligable for voting')
else:
    print('you are not eligable for voating')

#3. Write a program that takes a year as input and determines if it is a leap year using an if-else statement.
year = int(input('enter the year:'))
if ( year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('it is leap year')
else:
    print('it is not leap year')

#4. Write a program that takes the price of a product and the discount percentage as input and calculates the discounted price using an if-else statement.
price = int(input('enter the price :'))
discount_percentage = int(input('enter the discount:'))
discount_price = price - (price * discount_percentage / 100)
print(discount_price)
if discount_price < 0:
    print("Discount exceeds the price!")
else:
    print("Discounted price:", discount_price)

#5. Write a program that takes a character as input and determines if it is uppercase or lowercase using an if-else statement.
char = input('enter the charecter:')
if char.isupper():
    print('charecter s upper case')
elif char.islower():
    print('charecter is lower')
else:
    print('please enter the charecters')

        #or#
char = input('enter the charecter:')
if 'A' <= char <= 'Z':
    print('charecter s upper case')
elif 'a' <= char <='z':
    print('charecter is lower')
else:
    print('please enter the charecters')

#6. Write a program that takes a number as input and determines if it is positive, negative.
N = int(input('enter the number:'))
if N > 0:
    print('positive number')
else:
    print('negative number')

#1. Write a program that takes an integer as input and determines if it is even or odd using an if-else statement.
n = int(input('enter number:'))
if n % 2 == 0:
    print('even')
else:
    print('odd')

#pascals Traingle
rows = int(input("Enter the number of rows for Pascal's Triangle: "))

triangle = []


for i in range(rows):
    row = [1]  
    if triangle:
        last_row = triangle[-1]  
        for j in range(1, i):
            row.append(last_row[j - 1] + last_row[j])
        row.append(1)  
    triangle.append(row)
for row in triangle:
    for element in row:
        print(element, end=" ")
    print()  

    
    
    



